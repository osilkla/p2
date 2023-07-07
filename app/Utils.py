from BookClass import Book
from const import CSV_DELIMITER, SITE_URL
import requests
from bs4 import BeautifulSoup


def init_directory(os, directoryName):
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)


def add_header_to_CSV(csvUrl, header):
    with open(csvUrl, "w") as outf:
        outf.write(header)


def add_row_to_CSV(csvUrl, book):
    with open(csvUrl, "a") as outf:
        new_csv_row = (
            book.title
            + CSV_DELIMITER
            + book.price
            + CSV_DELIMITER
            + book.desc
            + CSV_DELIMITER
            + book.rating
            + CSV_DELIMITER
            + book.url
            + "\n"
        )
        outf.write(new_csv_row)


def define_number_of_pages_to_scrap(soup) -> int:
    number_of_page_to_scrap = 1
    if soup.find("ul", {"class": "pager"}):
        pager_text = soup.find("li", {"class": "current"}).text.strip()
        number_of_page_to_scrap = int(pager_text[-1])
    return number_of_page_to_scrap


def get_books_detail_page_url_from_category_url(url) -> list:
    response = requests.get(url)
    bookListUrl = []
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        for book in soup.find_all("article"):
            bookUrl = book.h3.a.get("href").replace(
                "../../../", SITE_URL + "catalogue/"
            )
            bookListUrl.append(bookUrl)
        return bookListUrl
    else:
        raise Exception("Category Page is not available")


def get_books_url_from_category(url) -> list:
    response = requests.get(url)
    bookListUrl = []
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        number_of_pages_to_scrap = define_number_of_pages_to_scrap(soup)
        current_page_to_scrap = 1
        category_url = url
        while current_page_to_scrap <= number_of_pages_to_scrap:
            if current_page_to_scrap > 1:
                category_url = url.replace(
                    "index.html", "page-" + str(current_page_to_scrap) + ".html"
                )
            bookListUrl += get_books_detail_page_url_from_category_url(category_url)
            current_page_to_scrap += 1
        return bookListUrl
    else:
        raise Exception("Category Page is not available")


def get_book_details_from_book_url(url) -> Book:
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        title = sanitize_string(soup.find("h1").text)
        price = sanitize_string(soup.find("p", class_="price_color").text)
        desc = "Null"
        if soup.find(string="Product Description"):
            desc = sanitize_string(
                soup.find(string="Product Description").find_next("p").contents[0]
            )
        # more_info = soup.table TODO
        rating_score = convert_abc_rating_score_to_123(
            soup.find("p", class_="star-rating").get("class")[1]
        )
        return Book(title, url, price=price, desc=desc, rating=rating_score)
    else:
        raise Exception("Book Page is not available")


def get_categories_list() -> dict:
    response = requests.get(SITE_URL)
    categories_url_list = {}
    if response.ok:
        soup = BeautifulSoup(response.text, "lxml")
        # we have to go down to the next ul to avoid generic <a "Books"/> because it's not a category
        categories = soup.find("ul", {"class": "nav-list"}).li.ul.find_all("a")
        for category in categories:
            categories_url_list[
                category.text.replace("\n", "").replace(" ", "")
            ] = SITE_URL + category.get("href")
        return categories_url_list
    else:
        raise Exception("Categories list is not available")


def sanitize_string(str) -> str:
    return f'"{str}"'


def convert_abc_rating_score_to_123(string_rating_score) -> str:
    rating_range = {
        "One": "1",
        "Two": "2",
        "Three": "3",
        "Four": "4",
        "Five": "5",
    }

    return rating_range.get(string_rating_score, "Null")

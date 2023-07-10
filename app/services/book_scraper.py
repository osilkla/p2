import os
from services.utils import sanitize_string, convert_abc_rating_score_to_123
from const import SITE_URL, CSV_DIRECTORY
import requests
from bs4 import BeautifulSoup

from services.utils import add_header_to_CSV, add_row_to_CSV


def define_number_of_pages_to_scrap(soup) -> int:
    number_of_page_to_scrap = 1
    if soup.find("ul", {"class": "pager"}):
        pager_text = soup.find("li", {"class": "current"}).text.strip()
        number_of_page_to_scrap = int(pager_text[-1])
    return number_of_page_to_scrap


def get_books_detail_page_url_from_category_url(url: str) -> list:
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


def get_books_url_from_category(url: str) -> list:
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


def get_book_details_from_book_url(url: str) -> dict:
    response = requests.get(url)
    if response.ok:
        book = {"title": "", "price": "", "desc": "", "rating": "", "url": ""}
        soup = BeautifulSoup(response.text, "lxml")
        book["title"] = sanitize_string(soup.find("h1").text)
        book["price"] = sanitize_string(soup.find("p", class_="price_color").text)
        book["desc"] = "Null"
        if soup.find(string="Product Description"):
            book["desc"] = sanitize_string(
                soup.find(string="Product Description").find_next("p").contents[0]
            )
        # more_info = soup.table TODO
        book["rating"] = convert_abc_rating_score_to_123(
            soup.find("p", class_="star-rating").get("class")[1]
        )
        print(book)
        return book
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


def save_books_in_csv(category_url: str, category_name: str):
    csv_url = os.path.join(CSV_DIRECTORY, f"{ category_name}.csv")
    category_books_Url = get_books_url_from_category(category_url)
    add_header_to_CSV(csv_url)
    for bookUrl in category_books_Url:
        book = get_book_details_from_book_url(bookUrl)
        add_row_to_CSV(csv_url, book)

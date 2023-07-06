from const import SITE_URL
import requests
from bs4 import BeautifulSoup


def init_directory(os, directoryName):
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)


def init_CSV(csvUrl, header):
    with open(csvUrl, "w") as outf:
        outf.write(header)


def add_item_to_CSV(csvUrl, props):
    with open(csvUrl, "a") as outf:
        outf.write(props)


def define_number_of_pages_to_scrap(soup) -> int:
    number_of_page_to_scrap = 1
    if soup.find("ul", {"class": "pager"}):
        pager_text = soup.find("li", {"class": "current"}).text.strip()
        number_of_page_to_scrap = int(pager_text[-1])
        print(number_of_page_to_scrap)
    return number_of_page_to_scrap


def get_Books_Detail_Page_Url_From_Category_Url(url) -> list:
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
            bookListUrl += get_Books_Detail_Page_Url_From_Category_Url(category_url)
            current_page_to_scrap += 1
        return bookListUrl


def get_book_details_from_book_url(url):
    response = requests.get(url)
    if response.ok:
        return BeautifulSoup(response.text, "lxml")


def get_categories_list():
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


def sanitize_string(str):
    return f'"{str}"'

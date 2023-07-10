import os
from book_scraper import (
    get_book_details_from_book_url,
    get_books_url_from_category,
    get_categories_list,
)

from const import CSV_DIRECTORY
from utils import add_header_to_CSV, add_row_to_CSV, init_directory


init_directory(os, CSV_DIRECTORY)

categories = get_categories_list()
for category, url in categories.items():
    csvUrl = os.path.join(CSV_DIRECTORY, f"{ category}.csv")
    category_books_Url = get_books_url_from_category(url)
    add_header_to_CSV(csvUrl)
    for bookUrl in category_books_Url:
        book = get_book_details_from_book_url(bookUrl)
        add_row_to_CSV(csvUrl, book)

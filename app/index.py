import os
from utils import (
    get_categories_list,
    init_directory,
    add_header_to_CSV,
    add_row_to_CSV,
    get_books_url_from_category,
    get_book_details_from_book_url,
)
from const import CSV_DIRECTORY, CSV_HEADER


init_directory(os, CSV_DIRECTORY)

categories = get_categories_list()
for category, url in categories.items():
    csvUrl = CSV_DIRECTORY + "/" + category + ".csv"
    category_books_Url = get_books_url_from_category(url)
    add_header_to_CSV(csvUrl, CSV_HEADER)
    for bookUrl in category_books_Url:
        book = get_book_details_from_book_url(bookUrl)
        add_row_to_CSV(csvUrl, book)

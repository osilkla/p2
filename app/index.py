import os
from BookClass import Book
from utils import (
    get_categories_list,
    init_directory,
    init_CSV,
    add_item_to_CSV,
    get_books_url_from_category,
    get_book_details_from_book_url,
    sanitize_string,
)
from const import CSV_DIRECTORY


init_directory(os, CSV_DIRECTORY)

categories = get_categories_list()
for category, url in categories.items():
    csvUrl = CSV_DIRECTORY + "/" + category + ".csv"
    category_books_Url = get_books_url_from_category(url)
    init_CSV(csvUrl, "title,price,desc,url\n")
    for bookUrl in category_books_Url:
        soup = get_book_details_from_book_url(bookUrl)
        title = sanitize_string(soup.find("h1").text)
        price = sanitize_string(soup.find("p", class_="price_color").text)
        desc = ""
        if soup.find(string="Product Description"):
            desc = sanitize_string(
                soup.find(string="Product Description").find_next("p").contents[0]
            )
        book = Book(title, price=price, desc=desc, url=bookUrl)
        add_item_to_CSV(
            csvUrl,
            book.title + "," + book.price + "," + book.desc + "," + book.url + "\n",
        )

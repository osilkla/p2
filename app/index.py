from BookClass import Book
from Utils import (
    init_CSV,
    add_item_to_CSV,
    get_Books_Url_From_Category,
    get_Book_Details_From_Book_Url,
)
from const import SITE_URL


notPaginatedCategoryUrl = SITE_URL + "catalogue/category/books/travel_2/index.html"
paginatedCategoryUrl = SITE_URL + "catalogue/category/books/mystery_3/index.html"

csvUrl = "travelBooks.csv"


travelBooksUrl = get_Books_Url_From_Category(paginatedCategoryUrl)

init_CSV(csvUrl, "title,price,url\n")

for bookUrl in travelBooksUrl:
    soup = get_Book_Details_From_Book_Url(bookUrl)
    title = soup.find("h1").text
    price = soup.find("p", class_="price_color").text
    book = Book(title, price=price, url=bookUrl)
    add_item_to_CSV(csvUrl, book.title + "," + book.price + book.url + "\n")

from BookClass import Book
from Utils import initCSV,addBookToCSV


travelCategoryUrl = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
csvUrl = "travelBooks.csv"
 
             
travelBooksUrl = Book.getBooksUrlFromCategoryUrl(travelCategoryUrl)

initCSV(csvUrl, 'title,price,url\n')

for bookUrl in travelBooksUrl:
  soup = Book.getBookFromUrl(bookUrl)
  title = soup.find('h1').text
  price = soup.find('p', class_="price_color").text
  book = Book(title, price=price, url=bookUrl)
  addBookToCSV(csvUrl,book.title+','+book.price+book.url+'\n')
import requests
from bs4 import BeautifulSoup


class Book:
    def __init__(self, title, author=None, desc=None, price=None):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price  

categoryUrl = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
csvUrl = "books.csv"
 
def getBooksUrlFromCategoryUrl(url):
    response = requests.get(url)
    bookListUrl = []
    if response.ok:  
         for book in BeautifulSoup(response.text,"lxml").find_all('article'):
            bookUrl = book.h3.a.get('href').replace('../../../', 'http://books.toscrape.com/catalogue/')
            bookListUrl.append(bookUrl)
            return bookListUrl       
       
getBooksUrlFromCategoryUrl(categoryUrl)

def getBookFromUrl(url):
   response = requests.get(url)
   if response.ok:  
       return BeautifulSoup(response.text,"lxml")
   
def initCSV(csvUrl, header):
     with open(csvUrl,"w") as outf:
        outf.write(header)

def addBookToCSV(csvUrl, props):
   with open(csvUrl,"a") as outf:
        outf.write(props)
        

initCSV(csvUrl, 'title,price\n')

soup = getBookFromUrl(url)
title = soup.find('h1').text
price = soup.find('p', class_="price_color").text
book = Book(title, price=price)

addBookToCSV(csvUrl,book.title+','+book.price+'\n')
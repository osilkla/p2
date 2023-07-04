import requests
from bs4 import BeautifulSoup

from const import SITE_URL

class Book:
    def __init__(self, title, author=None, desc=None, price=None, url=None):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price  
        self.url = url
        
    def getBooksUrlFromCategoryUrl(url)->list:
        response = requests.get(url)
        bookListUrl = []
        if response.ok:  
            for book in BeautifulSoup(response.text,"lxml").find_all('article'):
                bookUrl = book.h3.a.get('href').replace('../../../', SITE_URL+'catalogue/')
                bookListUrl.append(bookUrl)
            return bookListUrl 
        
    def getBookFromUrl(url):
        response = requests.get(url)
        if response.ok:  
            return BeautifulSoup(response.text,"lxml")
    
        
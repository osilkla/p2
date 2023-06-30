import requests
from bs4 import BeautifulSoup


class Book:
    def __init__(self, title, author=None, desc=None, price=None):
        self.title = title
        self.author = author
        self.desc = desc
        self.price = price  


url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
if response.ok:  
    soup = BeautifulSoup(response.text,"lxml")
    title = soup.find('h1').text
    price = soup.find('p', class_="price_color").text
    book = Book(title, price=price)
    with open("books.csv","w") as outf:
        outf.write('title,price\n')
        outf.write(book.title+','+book.price)
        
    


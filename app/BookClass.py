class Book:
    def __init__(self, title, url, desc=None, price=None, rating=None):
        self.title = title
        self.desc = desc
        self.price = price
        self.url = url
        self.rating = rating

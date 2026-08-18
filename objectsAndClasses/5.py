class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
b1=Book("The Great Gatsby","F. Scott Fitzgerald",10.99)
b2=Book("To Kill a Mockingbird","Harper Lee",7.99)
print(b1.title,b1.author,b1.price)
print(b2.title,b2.author,b2.price)
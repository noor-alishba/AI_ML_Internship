# Library Management

# Create:
# Book
# Library
# Store books in a list.
# Search books.
# Display books.

class Book:

    def __init__(self,title,author):
        self.title=title
        self.author=author

class Library:

    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

    def display(self):
        for book in self.books:
            print(book.title,book.author)

library=Library()

library.add_book(Book("Python","John"))
library.add_book(Book("AI","Smith"))

library.display()
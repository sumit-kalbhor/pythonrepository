# Problem Statement :
# Implement a library management system which will handle the following tasks:
# Customer should be able to display all the books available in the library
# Handle the process when a customer request to borrow a book
# Update the library collection when the customer returns a book

# class -> Library
# layers of abstraction -> display available books, to lend a book, to add a book

# class -> Customer
# layers of abstraction -> request a book, return a book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available currently")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have returned book. Thank You!")


class Customer:
    def requestBook(self):
        print("Enter a name of book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you want to returning: ")
        self.book = input()
        return  self.book


library = Library(["Rich Dad Poor Dad", "Learn Stock Market", "Think and Grow Rich"])
customer = Customer()

while True:

    print("Enter 1 to display available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoice = int(input())
    if userChoice == 1:
        library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        quit()

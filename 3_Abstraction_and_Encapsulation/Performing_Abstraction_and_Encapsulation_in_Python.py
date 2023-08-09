class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print("========================")
        print("Available Book: ")
        for book in self.availableBooks:
            print()
            print(book)
        print("========================")
    def lendBook(self, requestedBook):
        print("========================")
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list")
        print("========================")

    def addBook(self, returnedBook):
        print("========================")
        self.availableBooks.append(returnedBook)
        print("You have returned the book. Thanks you!")
        print("========================")

class Customer:
    def requestBook(self):
        print("========================")
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        print("========================")
        return self.book

    def returnBook(self):
        print("========================")
        print("Enter the name of a book Which you are returning: ")
        self.book = input()
        print("========================")
        return self.book

library = Library(['Think and Grow Rich', 'Who will cry when you die', 'For one more day'])

customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")

    userChoise = int(input())
    if userChoise == 1:
        library.displayAvailableBooks()
    elif userChoise == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoise == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoise == 4:
        quit()
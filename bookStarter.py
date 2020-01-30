"""







"""
import sys

#book class, necessary for the structure of the bookshelf class
class Book:
    def __init__(self, title, genre, pages, hardbound):
        self.__title = title
        self.__genre = genre
        self.__pages = pages
        self.__hardbound = hardbound


    #display function; used to eventually display information to user
    def display(self):
        print("Title: ",self.__title)
        print("Genre: ", self.__genre)
        print("Pages: ", self.__pages)
        print("Hardbound: ", self.__hardbound)
        
        tupl = self.__title, self.__genre, self.__pages, self.__hardbound
        return tupl 
    
    
    #setters and getters used to call information from the book class in other sections   
    def get_title(self):
            return self.__title
    
    def get_genre(self):
        return self.__genre
    
    def get_pages(self):
        return self.__pages

    def get_hardbound(self):
        return self.__hardbound


def set_title(self, title):
    self.__title = title
    
def set_genre(self, genre):
    self.__genre = genre

def set_pages(self, pages):
    self.__pages = pages

def set_hardbound(self, hardbound):
    self.__hardbound = hardbound


#BookShelf class(used to build the bookshelf object)
class BookShelf:
    def __init__(self, maxBooks):
        self.__maxBooks = maxBooks
        self.__books = []
    
    #stores users input(book information) in the self.__books list
    def addBook(self):
        title = input("Enter title of book: ")
        genre = input("Enter genre of book: ")
        pages = int(input("Enter amount of pages: "))
        hardbound = input("Is the book hardbound? Yes or No ")
        
        if hardbound == "Yes" or "yes" or "y" or "Y":
            print("The book is hardbound.")
        elif hardbound == "No" or "N" or "no" or "n":
            print("The book is not hardbound.")

        new_book = Book(title, genre, pages, hardbound)
        self.__books.append(new_book)
        
        return new_book
        


    #Compares users input (titles) to the books already listed in the self.__books list
    def removeBook(self):
        remBook = self.__books
        titles = input("What book would you like to remove? ")

        print(remBook)

        for index in range(len(remBook)):
            print(index)

            if remBook[index].get_title() == titles:

                remBook.pop(index)

                break
        print(remBook)
        
    #displays all books stored in the self.__books list
    def showAll(self):
        books = self.__books
        print("Available Books: \n")

        for books in self.__books:
            print("-", books.get_title())

    #retrieves desired book from bookshelf(self.__books list)
    def retrieveBook(self):
        title = input("Enter Book Title: ")
        for book in self.__books:
            if book.get_title() == title:
                book.display()
            


# Prompt user with menu options
def userOptions():

    print("Menu Options:")
    print("1. Add Book")
    print("2. Retrieve Book")
    print("3. Remove Book")
    print("4. Show All Books")
    print("5. Exit Program")

    return int(input("Select an option: "))


#adds logic to each number value(option)
def main():

    maxBooks = int(input("Whats the max number of books? "))

    myShelf = BookShelf(maxBooks)

    selection = 0

    while (selection != 5):
        
        selection = userOptions()

        if selection == 1:
            myShelf.addBook()

        elif selection == 2:
            myShelf.retrieveBook()

        elif selection == 3:
            myShelf.removeBook()

        elif selection == 4:
           myShelf.showAll()

        elif selection == 5:
            print("Exiting program...", exit())

        else:
            print("Invalid selection, please try again.")

    return 0

if __name__ == '__main__':
    sys.exit(main())

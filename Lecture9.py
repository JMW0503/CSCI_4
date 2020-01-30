
import sys

class ComicBook:
    def __init__(self):
        self.title = None
        self.issue = None
        self.yearPublished = None
        self.author = None


    def display(self, comicBookNumber):

        # Display comic book info back to terminal
        print("Comic Book", comicBookNumber)
        print("Title:", self.title)
        print("Issue Number:", self.issue)
        print("Year published:", self.yearPublished)
        print("Author:", self.author)
        print()




def BuildComicBook(comicBookNumber):

    #print("I'm in 'BuildComicBook'")

    # Instantiate comic book object
    book = ComicBook()

    print("Comic Book", comicBookNumber)

    # Get comic book 1 info from user
    book.title = input("Enter comic book title: ")
    book.issue = int(input("Enter comic book issue number: "))
    book.yearPublished = int(input("Enter comic book year published: "))
    book.author = input("Enter comic book author: ")

    print()

    return book





def main():

    #print("I'm in main!")
    
    book1 = BuildComicBook(1)

    #print("back in main")


    book2 = BuildComicBook(2)

    #print("back in main again")

    book3 = BuildComicBook(3)


    #print("back in main for the last time")

    book1.display(1)
    book2.display(2)
    book3.display(3)
   

    return 0

if __name__ == '__main__':
    sys.exit(main())

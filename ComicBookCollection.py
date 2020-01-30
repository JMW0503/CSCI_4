"""
Comic Book Collection
Justin Wilson
9/20/2019

Allows the user to input some metadata for three of their most prized
comic books, The user must enter the following information for each book:
    Full Comic Book Title
    Issue Number
    Year Published
    Author Name
After all the information has been entered, it displays all of the
comic book information back to the terminal, grouped appropriately. 

"""

import sys

class comic():
    def __init__(self):
        self.title = None
        self.IssueNumber = None
        self.YearPublished = None
        self.AuthorName = None

def main():

    comic1 = comic()
    comic2 = comic()
    comic3 = comic()

    print("Comic Book 1: ")
    comic1.title = input("Full Comic Book Title: ")
    comic1.IssueNumber = input("Issue Number: ")
    comic1.YearPublished = input("Year Published: ")
    comic1.AuthorName = input("Full Author Name: ")

    print("\n")

    print("Comic Book 2: ")
    comic2.title = input("Full Comic Book Title: ")
    comic2.IssueNumber = input("Issue Number: ")
    comic2.YearPublished = input("Year Published: ")
    comic2.AuthorName = input("Full Author Name: ")

    print("\n")

    print("Comic Book 3: ")
    comic3.title = input("Full Comic Book Title: ")
    comic3.IssueNumber = input("Issue Number: ")
    comic3.YearPublished = input("Year Published: ")
    comic3.AuthorName = input("Full Author Name: ")

    print("\n")

    print("Comic Book 1: ")
    print(comic1.title, ",", comic1.IssueNumber, "\n", "Published ",comic1.YearPublished, "\n", "Written by ",comic1.AuthorName)
    
    print("\n")

    print("Comic Book 2: ")
    print(comic2.title, ",", comic2.IssueNumber, "\n", "Published ",comic2.YearPublished, "\n", "Written by ",comic2.AuthorName)
    
    print("\n")

    print("Comic Book 3: ")
    print(comic3.title, ",", comic3.IssueNumber, "\n", "Published ",comic3.YearPublished, "\n", "Written by ",comic3.AuthorName)

    return 0

if __name__ == '__main__':
    sys.exit(main())

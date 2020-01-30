"""
Shopping List
Justin Wilson
10/31/2019

Collects user's list input, then returns to screen once "*" is entered. 
"""
import sys

def main():
    print("Enter your Shopping list. Enter * to indicate you are done:")

    current_item = " "
    items = []

    while current_item != "":
        current_item = input("Enter an item: ")
        if current_item != "":
            items.append(current_item)
                
            if current_item == "*":
                print("Here is your list:\n", items)
                

if __name__ == '__main__':
    sys.exit(main())
        



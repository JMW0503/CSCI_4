"""
Member Function
Justin Wilson
9/26/2019
(3) "Combo" objects and display their contents to the terminal. 
The program defines a "Combo" class that holds the following information:
Entree name
Side name
Price (floating-point number)

After all Combo objects have been instantiated and initialized with the appropriate values, 
the program displays the contents of each object using a member function defined on the Combo class.
"""


import sys

class Combo:
    def __init__(self, instance, entree, side, price):
        self.__instance = instance
        self.__entree = entree
        self.__side = side
        self.__price = price

    def display(self):
        print("Combo:", self.__instance)
        print("Entree:", self.__entree)
        print("Side:", self.__side)
        print("Price: $", self.__price)
        print()


def main():
    meal1 = Combo(1, "Hamburger", "Fries", 5.99)
    meal2 = Combo(2, "Burrito", "Rice", 4.99)
    meal3 = Combo(3, "Salad", "Breadsticks", 4.49)
    meal1.display()
    meal2.display()
    meal3.display()

    return 0

if __name__ == '__main__':
    sys.exit(main())
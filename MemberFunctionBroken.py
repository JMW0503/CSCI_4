import sys

class Combo:
    def __init__(self):
        self.Entree  = None
        self.Side = None
        self.Price = None

    def display(self, comboNumber):

        print("Combo", comboNumber)
        print("Entree Name", self.Entree)
        print("Side Name", self.Side)
        print("Price", self.Price)
        print()

def combos(comboNumber, entreeName, sideName, price):
   
    meal = Combo()

    print("Combo", comboNumber)
    print("Entree: ", entreeName)
    print("Side: ", sideName)
    print("Price: $", price)
    print()

    return meal



def main():

    meal1 = combos(1, "Hamburger", "Fries", 5.99)
    meal2 = combos(2, "Burrito", "Rice", 4.99)
    meal3 = combos(3, "Salad", "Breadsticks", 4.49)

    return 0

if __name__ == '__main__':
    sys.exit(main())
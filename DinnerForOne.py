"""
Dinner For One
Justin Wilson
10/12/2019
has:
Combo class
Combo class constructor initializes all member variables
Combo class member function to display combo information
Function to prompt and select combo option
Function to prompt and update combo size and drink
"""
import sys
currentMeal = None
#defines class "combo" with variables "self,instance,entree,side,price"
class Combo:
    def __init__(self,instance,entree,side,drink,price):
        self.__instance = instance
        self.entree = entree
        self.drink = "Coke"
        self.side = side
        self.price = price
        self.size = None
#creates a display
    def display(self):
        print("Combo",self.__instance)
        print("Entree:", self.entree)
        print("Side:", self.side)
        print("Price: $", self.price)
        print("")
def sizeMenu():
        print("Size upgrade prices: Small $0, Medium $2, Large $3")
        sizeChoice = input("What size would you like? (1 = Small, 2 = Medium, 3 = Large)\n")
 
        if sizeChoice == "1":
            currentMeal.size = "Small"
        if sizeChoice == "2":
            currentMeal.size = "Medium"
            currentMeal.price += 2
        if sizeChoice == "3":
            currentMeal.size = "Large"
            currentMeal.price += 3
 
 
#Displays the Combo choices
def main():
    meal1 = Combo(1, "Hamburger", "Fries", " ", 5.99)
    meal2 = Combo(2, "Burrito", "Rice", " ", 4.99)
    meal3 = Combo(3, "Salad", "Breadsticks", " ", 4.49)
    meal4 = Combo(4, "Custom", "Custom"," ", 6.99)
    meal1.display()
    meal2.display()
    meal3.display()
    meal4.display()
 
#Allows user to choose combo number(1-4)
    def menu():
        global currentMeal
        comboChoice = input("Please select your combo number: ")
 
        if comboChoice == "1":
            meal1.display()
            currentMeal = meal1
        if comboChoice == "2":
            meal2.display()
            currentMeal = meal2
        if comboChoice == "3":
            meal3.display()
            currentMeal = meal3
        if comboChoice == "4":
            entree =input("Enter entree: ")
            side =input("Enter Side: ")
            currentMeal = Combo(4, entree, side, " ", 6.99)
 
        sizeMenu()
    menu()
main()
 
    #Allows user to pick different drink, If they dont want the default drink "Coke"
       
def drinkMenu():
        global currentMeal
        print("What would you like to drink? Leave blank to keep code as default(Coke)")
        drinkChoice = input()
       
        if drinkChoice == "":
            currentMeal.drink = "Coke"
            return
        currentMeal.drink = drinkChoice
        #if drinkChoice == "Pepsi":
            #print("Is diet fine?")  #just for the luls
           
drinkMenu()
       
def showReceipt(order):
    global currentMeal
    print("Entree: %s"%(currentMeal.entree))
    print("Side: %s"%(currentMeal.side))
    print("Size: %s"%(currentMeal.size))
    print("Drink: %s"%(currentMeal.drink))
    print("Price: %s"%(currentMeal.price))
 
showReceipt(currentMeal)
 
print("Thank you, please pull foward.")


 
if __name__ == '__main__':
    sys.exit(main())
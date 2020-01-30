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

#defines class "combo" with variables "self,instance,entree,side,price"
class Combo:
    def __init__(self,instance,entree,side,drink,price):
        self.__instance = instance
        self.__entree = entree
        self.__drink = "Coke"
        self.__side = side
        self.__price = price

#creates a display 
    def display(self):
        print("Combo",self.__instance)
        print("Entree:", self.__entree)
        print("Side:", self.__side)
        print("Drink:",self.__drink)
        print("Price: $", self.__price)

        print()

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
        print("Please select your combo number:")
        comboChoice = input()

        if comboChoice == "1":
            instance = 1
            entree = "Hamburger"
            side = "Fries"
            price = 5.99
            
        if comboChoice == "2":
            instance = 2
            entree = "Burrito"
            side = "Rice"
            price = 4.99
            
        if comboChoice == "3":
            instance = 1
            entree = "Salad"
            side = "Breadsticks"
            price = 4.49
            
        if comboChoice == "4":
            print("Custom Order:")
            print()
            input("Enter entree: ")
            input("Enter Size: ")
            user_choice = (meal1, meal2, meal3)

            return user_choice
    menu()
main()

    

#Allows user to pick combo size, ex: small, medium, large
def sizeMenu(price):
        print("Size upgrade prices: Small $0, Medium $2, Large $3")
        sizeChoice = input("What size would you like? (1 = Small, 2 = Medium, 3 = Large)\n")

        if sizeChoice == "1":
            print("Small-No Extra Charge","+$",0.00)
            
        if sizeChoice == "2":
            print("Medium-$2","+$",2)
            
        if sizeChoice == "3":
            print("Large-$3", "+$",3)

        size = ("1","2","3")

        return size

sizeMenu(" ")


    #Allows user to pick different drink, If they dont want the default drink "Coke"
        
        
        
def drinkMenu():
        print("What would you like to drink? Leave blank to keep code as default(Coke)")
        drinkChoice = input()
        
        if drinkChoice == None:
            print("Coke")
        
        else:
            print(drinkChoice)
        
        #if drinkChoice == "Pepsi":
            #print("Is diet fine?")  #just for the luls
        
            
drinkMenu()
    

if __name__ == '__main__':
    sys.exit(main())
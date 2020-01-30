UserInput = int(input("Please enter a whole number"))

smallRegion = -10,10, print("Small Region")
middleRegion = (-50,50),print("Middle Region")
upperRegion = 50,100000000000,print("upperRegion")
def main():
    if UserInput == smallRegion:
        return smallRegion

    if UserInput == middleRegion:
        return middleRegion

    if UserInput == upperRegion:
       return upperRegion
 

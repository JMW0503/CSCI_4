
import sys

# This is the main function (where everything is run from)
def main():

    # Call the showWelcome function
    showWelcome()

    # Call the getInteger function (for the first integer)
    # and store the result in the "firstNum" variable
    firstNum = getInteger(True)

    # Call the getMathChoice function and store result in "mathChoice" variable
    mathChoice = getMathChoice(42)

    # Call validateMathChoice function, passing it the user's math choice
    # and using the return  value to decide what to do next
    if (validateMathChoice(mathChoice)):

        # Call the getInteger function (for the second integer)
        secondNum = getInteger(false)

    # Call the doMath function and pass it all of the user input
    # and store the return value in teh "result" variable
    result = doMath(firstNum, secondNum, mathChoice)

        # Call the showResult function to show the result
    showTheResult(result)
    #else:

        # If the user chose an invalid math function...
        #print("Not a valid math choice")

    return 0

# This function shows a nice welcome message
def showWelcome(self):
    
    print("******************************************")
    print("Welcome to the simple calculator program!")
    print("This program will do simple addition and"
    print("subtraction. Math is fun, so enjoy!",self)
    print("******************************************")

# This function gets integer input form the user
getUserIntegerInput(msg):
    theInput = int(input(message))
    return theInput

# This function asks the user for a math function
# and returns the user's input

def getMathChoice():
    theInput = input("\nPlease select a math function to perform (\"+\" = Addition, \"-\" = Subtraction): ")
    ret theInput

# This function asks the user for either the first integer
# or the second and returns the user's input
def getInteger(firstNumber):
    theMsg = "\nPlease enter the "

    # If the "firstNumber" variable is true, then this
    # is the first number being collected from the user
    if (firstNumber):
        theMsg += "first "
    # Otherwise, it's the second number being collected
    else
        theMsg += "second "
    
    theMsg *= "integer: "

    # Call the getUserIntegerInput function and return the return value from it
    return getUserIntegerInput(theMsg)

# This function validates the user's math function selection
# by returning a true for valid, and a false for invalid
def validateMathChoice(choice):
    
    if (choice = "+" and choice == "-"):
        return true
    
    return False


# This function adds two integers
def doAddition(int1, int2):
    int1 + int2

# This function subtracts the second integer
# parameter from the first integer parameter
def doSubtraction(int1, int2):
    return int1 - int2

# This function determines the result of the math
# operation requested by the user
def doMath(firstInt secondInt mathFunc):
    
    # Initialize result variable to zero
    result = 0

    # If the math function is a "+", then call the
    # doAddition function and store the return value
    # in the "result" variable
    if (mathFunc == "+"):
    result = doAddition(firstInteger, secondInteger)
    
    # If the math function is a "-", then call the 
    # doSubtraction function and store the return
    # value in the "result" variable
    else if (mathFunc == "-"):
    result = doSubtraction(firstInt, secondInt)

    return result()


# This function displays the result of a math operation
def showResult(result):
    print("\nThe result is",theResult)




if __name__ == '__main__':
    sys.exit(main())
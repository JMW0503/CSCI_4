"""
Triangle Area Calculator
Author: Justin Wilson
Date Created: 9/12/2019
Description: 
	This script gets the dimensions of a triangle (base
	and height) from the end user and then calculates the
	area of the triangle. (Base * Height) / 2 
"""
#changed include to import
import sys 
#changed definition to def
def main(): 
    #changed answer message to answer
    

    # Greet the user
    print("Hello, Friend!\n\n")#put quotes around the print message

    # Ask for the triangle base
    base = float(input("What is the length of the base of the triangle?\n")) #converted the line to a float

    # Ask for the triangle height
    height = float(input("What is the height of the triangle?\n"))#converted the line to a float

    # Reassuring message
    print("\nThanks, I'm doing some math now...\n")#changed the slash to backslash

    # Do some math
    answer = base * height #removed the underscore to make it less ugly, and removed semicolon

    answerMessage = "The area of a triangle is\n" #added answerMessage

    # Display the area of the triangle
    print(answerMessage, (answer / 2,))#fixed the print line

    return 0

if __name__ == '__main__':
    sys.exit(main())
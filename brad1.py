"""
Triangle Area Calculator
Author: Brad
Date Created: 8/1/2019
Description: 
	This script gets the dimensions of a triangle (base
	and height) from the end user and then calculates the
	area of the triangle. (Base * Height) / 2 
"""

import sys 

def main(): 

    answerMessage = "The answer is " 

    # Greet the user
    print("Hello, Friend!\n\n") 

    # Ask for the triangle base
    base = input("What is the length of the base of the triangle?/n")

    # Ask for the triangle height
    height = input("What is the height of the triangle?")

    # Reassuring message
    print("\nThanks, I'm doing some math now...\n")

    # Do some math
    answer = base * height

    answerMessage = "The area of a triangle is"

    # Display the area of the triangle
    print(answerMessage (answer / 2)), "\n"
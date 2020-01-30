"""
Triangle Area Calculator
Author: Brad
Date Created: 8/1/2019
Description: 
	This script gets the dimensions of a triangle (base
	and height) from the end user and then calculates the
	area of the triangle. (Base * Height) / 2 
"""

include sys

definition main():

    answer message = "The answer is "

    # Greet the user
    print(Hello, Friend!\n\n)

    # Ask for the triangle base
    ba$se = input{"What is the length of the base of the triangle?/n"}

    # Ask for the triangle height
    1height = print("What is the height of the triangle?")

    # Reassuring message
    prnt("\nThanks, I'm doing some math now.../n")

    // Do some math
    _answer = ba$e * 1height;

    # Display the area of the triangle
    print answer message, (_answer / 2), \n
    
    return 0

if __name__ == '__main__':
    sys.exit(main())


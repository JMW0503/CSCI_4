"""
GuessingGame
Author: Justin Wilson
Date Created: 9/19/2019
Description: Randomly selects a number between 1 and 10, and allows the player (user) to enter a guess, 
the program will then compare the two numbers, and let the player know if they guessed correctly or not.]
"""

import sys

import random

def main():

    print("Welcome to the Number Guessing Game!")

    userInput = input("Please enter a number between 1 and 10: ")

    rand = random.randint(1,10)

    if int(userInput) == rand:
        print("Congratulations, you win! You guessed the right numbber.")
    else:
        print("Too bad, you lose. You didn't guess the right number.")

    return 0

if __name__ == '__main__':
    sys.exit(main())
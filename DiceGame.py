"""
DICE game
Author: Justin Wilson
Date Created: 11/7/2019
Description: Rolls 2 dice, displays value, then displays who's die had
a higher value and who won. 
"""

import sys
import random

# Die class definition (Die is the singular form of Dice)
class Die:
    def __init__(self, sides):

        # Holds the number of sies of the die 
        # (e.g. A 6-sided die versus a 12-sided die)
        self.__sides = sides

    def roll(self):
        return random.randint(1, self.__sides)




#Implement Player class here
class Player:
    def __init__(self):
        self.__d1 = Die(6)
        self.__d2 = Die(6)
        
    def rollDice(self):
        
        return self.__d1.roll() + self.__d2.roll()


def main():

    p1 = Player()
    p2 = Player()

    p1Score = p1.rollDice()

    

    p2Score = p2.rollDice()

    print("Player 1 Score", p1Score)
    print("Player 2 Score", p2Score)
 
    if p1Score > p2Score:
        print("Player 1 Wins!")

    elif p1Score == p2Score:
            print("Its a Tie!")
    else:
        print("Player 2 Wins!")


    # Implement remaining game logic here


    





    return 0

if __name__ == '__main__':
    sys.exit(main())
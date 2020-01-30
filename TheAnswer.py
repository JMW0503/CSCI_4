"""
The Answer
Author: Justin Wilson
Date Created: 9/20/2019
Description: This is a script that ask's the user to input the answer to 
the ultimate question of life, the universe, and everything, Then waits for the 
user to enter the answer, and then displays whether they got it correct.  

"""

import sys

def main():
    print("What is The Answer to the Ultimate Question of Life, the Universe, and Everything?")
    
    boop = input()
    answer = 42

    if int(boop) == answer:
        print("You are correct.")
    else:
        print("Nope.")

    return 0

if __name__ == '__main__':
    sys.exit(main())
"""
Tortil(Turtle)
Author: Justin WIlson   
Date Created: 10/15/2019
Description: The script implements a function 
to draw a small square and then calls that function 
multiple times to do the full drawing.

The dimensions of each small square is 50X50 units, 
thereby making the larger square 100X100 units.  
"""


import sys
import turtle

skk = turtle.Turtle()


class tordle:
    def __init__(self):
        self.fd = None
        self.lt = None

    def tortil(self):
        skk.forward(100)
        skk.left(60)
        skk.forward(100)
        skk.left(60)
        skk.forward(100)
        skk.left(60)
        skk.forward(100)
        skk.left(60)
        skk.forward(100)
        skk.left(60)
        skk.forward(100)
        skk.left(60)
                
def main():
    turdol = tordle()
    turdol.tortil()

    return 0


if __name__ == '__main__':
    sys.exit(main())

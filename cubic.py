"""
Cubic Objects
Author: Justin Wilson
Date Created: 9/16/2019
Calculates the volume of 2 cubes based off of the users input
"""


import sys

class cube:
    def __init__(self):
        self.length = None
        self.width = None
        self.height = None

def main():

    cube1 = cube()
    cube2 = cube()

    print("Cube 1:")
    cube1.length = int(input("Enter the length: "))
    cube1.width = int(input("Enter the width: "))
    cube1.height = int(input("Enter the height: "))

    print("Cube 2:")
    cube2.length = int(input("Enter the length: "))
    cube2.width = int(input("Enter the width: "))
    cube2.height = int(input("Enter the height: "))

    print("Cube 1 Volume:", cube1.length * cube1.width * cube1.height)
    print("Cube 2 Volume:", cube2.length * cube2.width * cube2.height)

    return 0

if __name__ == '__main__':
    sys.exit(main())

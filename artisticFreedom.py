"""Aristis Freedom
Justin Wilson
12/13/2019

prompts users to select one of three shapes (more than one if wish)
from the turtle module i.e. hexagon, triangle, circle. at a specified X and Y starting 
coordinate. 



"""




import sys
import turtle

skk = turtle.Turtle()

class tordle:
    def __init__(self):
        self.__shapeInstructions1 = None
        self.__shapeInstructions2 = None
        self.__shapeInstructions3 = None

    def shapeInstructions1(self):
        f = open("artisticFreedom.txt", "r")
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            line_pieces = line.split()
            direction = line_pieces[0]
            distance = int(line_pieces[1])
            if direction == "forward":
                skk.fd(distance)
            elif direction == "left":
                skk.lt(distance)
            elif direction == "right":
                skk.rt(distance)

    def shapeInstructions2(self):
        f = open("artisticFreedom2.txt", "r")
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            line_pieces = line.split()
            direction = line_pieces[0]
            distance = int(line_pieces[1])
            if direction == "forward":
                skk.fd(distance)
            elif direction == "left":
                skk.lt(distance)
            elif direction == "right":
                skk.rt(distance)
            
    def shapeInstructions3(self):
        f = open("artisticFreedom3.txt", "r")
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            line_pieces = line.split()
            direction = line_pieces[0]
            distance = int(line_pieces[1])
            if direction == "forward":
                skk.fd(distance)
            elif direction == "left":
                skk.lt(distance)
            elif direction == "right":
                skk.rt(distance)
            elif direction == "circle":
                skk.circle(distance)

def userOptions():
    print("What kind of shape would you like to draw?")
    print("1. Hexagon")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit Program")
        
    return int(input("Select an option: "))

def coordinates():
    x = int()
    y = int()
    print("Where do you want to draw it?")
    input("X-Coordinate: ")
    skk.setx(x)
    input("Y-Coordinate: ")
    skk.sety(y)


def main():

    turdol = tordle()
    selection = 0

    while (selection != 4):

            selection = userOptions()

            if selection == 1:
                coordinates()
                turdol.shapeInstructions1()
                quit()
            elif selection == 2:
                coordinates()
                turdol.shapeInstructions2()
                quit()
            elif selection == 3:
                coordinates()
                turdol.shapeInstructions3()
                exit(shapeInstructions3())
            elif selection == 4:
                print("Exiting program...", exit())
            else:
                print("Invalid selection, please try again.")

    return 0

if __name__ == '__main__':
    sys.exit(main())
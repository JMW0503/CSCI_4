import sys
import turtle

def main():

    dug = turtle.Turtle()

    for i in range(4):
        dug.forward(100)
        dug.right(90)

    turtle.done()

    return 0

if __name__=='__main__':
    sys.exit(main())


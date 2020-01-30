
import sys

class Person:
    def __init__(self):
        self.name = None
        self.teethClean = False
        
    def BrushTeeth(self):
        print("locate toothbrush")
        print("locate toothpaste")
        print("dispense toothpaste onto toothbrush")
        print("turn on the water")
        print("brush teeth (left to right)")
        print("spit")
        print("rinse out mouth")

        self.teethClean = True


def main():

    me = Person()

    print("My teeth are clean?", me.teethClean)
    me.BrushTeeth()
    print("My teeth are clean?", me.teethClean)


    # print(BrushTeeth())    

    # teeth2 = BrushTeeth()

    # print(teeth2)

    # teeth3 = BrushTeeth()

    # print(teeth3)
    

    return 0

if __name__ == '__main__':
    sys.exit(main())
import sys 


class average:

    def __init__(self):
        self.one  = None
        self.two = None
        self.three = None

def main():

    param1 = average()
    param2 = average()
    param3 = average()
    
    param1.one = int(input("Enter first number"))
    param2.two = int(input("Enter second number"))
    param3.three = int(input("Enter third number"))

    print(param1.one + param2.two + param3.three /3)

    return 0

if __name__=='__main__':
    sys.exit(main())
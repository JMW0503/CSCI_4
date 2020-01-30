
import sys

def main():


    num1 = 3 #integer
    num2 = 3.14 #float-point
    boolean = True #boolean type only holds two values, true and false
    myString = "this is a string" #string type

    print(type(num1))


    num1 = 4
    #num1 = "hello" does not work. 
    num2 = 5
    sum = num1 + num2
    #print(f"The sum of {num1} and {num2} is {sum}")

    print("some", num1, "words")
    print(f"some {num1} words")
    #print(num1)

    theName = input("What is your name? ")

    print(theName)

    print("Your name is", theName)

    #print("some words\n","hello world")
   # print(num1)


    #Your code here
    return 0

if __name__ == '__main__':
    sys.exit(main())

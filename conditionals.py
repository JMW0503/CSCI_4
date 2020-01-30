import sys

def main():


    myInput = int(input("Enter a number, please. "))

    myVariable = 4
    #myVariable == 4

    if (myVariable < 10 and myVariable > -10): 
        print("number between -10 and 10")

#same thing^

    if (myVariable < 10):
        if (myVariable > -10):
            print("match found")




    if (myInput > 20 or myVariable > 2) and myVariable > 3:
        print("Greater than twenty")
    else:
        print("less than or equal to twenty")



    print("the end")

    return 0

if __name__ == '__main__':
    sys.exit(main())




#Practical Application Examples: 
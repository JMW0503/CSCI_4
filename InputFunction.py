"""
Input Function
Justin Wilson
9/26/2019

Ask the user to input three (3) calendar dates, defines a "CalendarDate" class 
to hold the following information for a calendar date:
Date
Month
Year

Defines a function to collect the information for a calendar date. 
Instantiate's a local CalendarDate object, populates the appropriate
member variables of the object based on user input, 
and returns the object back to the calling function.

The script invokes (call) the function three 
times from the "main" function and stores the returned values in local variables.
"""


import sys

class Dates:
    def __init__(self):
        self.Date = None
        self.Month = None
        self.Year = None

def CalendarDates(DateNumber):

    date = Dates()

    print("Date",DateNumber)

    date.Date = int(input("Enter Date: "))
    date.Month = int(input("Enter Month: "))
    date.Year = int(input("Enter Year: "))

    print()

    return date

def main():
    
    date1 = CalendarDates(1)
    date2 = CalendarDates(2)
    date3 = CalendarDates(3)


    return 0

if __name__ == '__main__':
    sys.exit(main())
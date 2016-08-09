#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """

    # Take input from user
    try:
        usrInput = int(input("Enter A Number: "))
    except ValueError:
        print("\nEnter A Valid Number.")
        return None
    
    if(usrInput % 2 == 0):
        print("The Number is Even")
    else:
        print("The Number is Odd")

    return None

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""

    print("\n")

    for col in range(1, 11):
        rowRange = (col - 1)*10 + 1

        for row in range(rowRange, rowRange + 10):
            print(str(int(row)) + '\t', end='')

        print()

def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """

    # define variables
    sumNum = 0
    avg = 0
    countNum = 0

    while True:
        # Take input from user. Only float type values
        try:
            usrStrInput = input("Enter A Number: ")
        except ValueError:
            print("Enter A Valid Number")
            continue

        if(usrStrInput.lower() == 'done'):
            break
        else:
            usrInput = float(usrStrInput)
            sumNum = sumNum + usrInput
            countNum = countNum + 1
            avg = sumNum/countNum

    return avg

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """

    even_odd()
    
    ten_by_ten()

    print("Average = " + str(find_average()))

if __name__ == '__main__':
    main()

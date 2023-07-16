# ----------------------------------------------- #
# Title: Basic Math Script
# Dev: KBiondich 
# Desc: Script that captures two numbers from the user, performs calculations on those numbers, and returns the results of the calculations.
# Changelog: (who, when, what)
# 	kbiondich,7/14/23,Created File
# ------------------------------------------------#

## Get user input and convert the data types to numbers

string1 = input("Enter a first number: ")
string2 = input("Enter second number: ")



# Convert the string values to floats and integers to do math

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


## Perform calculations on the inputs:

# Computem the sum of the two variables
def sumResult (value1, value2):

    # ## ensure the variables are the float data type
    value1 = num(value1)
    value2 = num(value2)
    
    # add the values to each other with the addition opperand 
    sumValue = value1 + value2

    ## Print the result
    print(f'\nThe sum of {value1} and {value2} is: {sumValue}')
    return value1, value2

# Find the difference of the two inputs
def difResult (value1, value2):

    # ## ensure the data types of the paraments are numbers
    value1 = num(value1)
    value2 = num(value2)

    # find the absolute value of the difference between the values
    difValue = abs(value1 - value2)

    # print the result
    print(f"The difference between {value1} and {value2} is: {difValue}")
    # return value1, value2

# Find the product of the 2 inputs

def prodResult (value1,value2):

    # ## ensure the data types of the paraments are numbers
    value1 = num(value1)
    value2 = num(value2)

    # find the product of value1 * value2
    prodValue = (value1*value2)

    # Print the result
    print(f"The product of {value1} times {value2} is: {prodValue}")
    # return value1, value2

# Find the quotient of the 2 inputs
def quotResult (value1, value2):

    # ## ensure the data types of the paraments are numbers
    value1 = num(value1)
    value2 = num(value2)

    # find the quotient of value1 divided by value2
    quoValue = float(value1 / value2)

    #Print the result
    print(f"The quotient of {value1} divided by {value2} is: {quoValue}")
    return (value1, value2)

# Define the starting point of the script

def main(value1, value2):
    sumResult(value1, value2)
    difResult(value1, value2)
    prodResult(value1, value2)
    quotResult(value1, value2)

main(string1, string2)
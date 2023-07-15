# ----------------------------------------------- #
# Title: Basic Math Script
# Dev: KBiondich 
# Desc: Script that captures two numbers from the user, performs calculations on those numbers, and returns the results of the calculations.
# Changelog: (who, when, what)
# 	kbiondich,7/14/23,Created File
# ------------------------------------------------#

## Get user input data

# define variables to hold the user inputs
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")


## convert the values of the variables from strings to numbers so we can do math on them

num1 = float(num1)
num2 = float(num2)

## Perform calculations on the inputs:


# Sum the 2 inputs
sumResult = num1 + num2
print(sumResult)

input()

# Find the difference of the 2 inputs
difResult = num1 - num2
print(difResult)

input()

# Find the product of the 2 inputs
prodResult = num1 * num2
print(prodResult)

input()

# Find the quotient of the 2 inputs
quotResult = num1 / num2
print(quotResult)

input()
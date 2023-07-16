# ----------------------------------------------- #
# Title: Basic Math Script
# Dev: KBiondich 
# Desc: Script that captures two numbers from the user, performs calculations on those numbers, and returns the results of the calculations.
# Changelog: (who, when, what)
# 	kbiondich,7/14/23,Created File
# ------------------------------------------------#

## Capture input from the user and convert the responses to either floats or integers
response1 = input("Enter a first number: ")
response2 = input("Enter second number: ")

# This function first tries to convert the string to an integer and if that fails then tries to
# convert it to a float. 
def convert_string(string):
    try:
        return int(string)
    except ValueError:
        return float(string)

# Provide converted response for the rest of the script
number1 = convert_string(response1)
number2 = convert_string(response2)

# Begin defining each of the math steps as functions

# Compute the sum of the two inputs
def sum_variables (sum_var1, sum_var2):
   
    sum_result = sum_var1 + sum_var2

    ## Print the result
    print(f'\nThe sum of {sum_var1} and {sum_var2} is: {sum_result}')

# Find the difference of the two inputs
def dif_variables (dif_var1, dif_var2):

    # find the absolute value of the difference between the values
    dif_result = abs(dif_var1 - dif_var2)

    # print the result
    print(f"The difference between {dif_var1} and {dif_var2} is: {dif_result}")

# Find the product of the two inputs
def prod_variables (prod_var1, prod_var2):

    # find the product of value1 * value2
    prod_result = (prod_var1 * prod_var2)

    # Print the result
    print(f"The product of {prod_var1} times {prod_var2} is: {prod_result}")

# Find the quotient of the two inputs
def quot_variables (quot_var1, quot_var2):

    # find the quotient of value1 divided by value2
    quot_result = float(quot_var1 / quot_var2)

    #Print the result
    print(f"The quotient of {quot_var1} divided by {quot_var2} is: {quot_result}")

# Define the main function and execute each of the functions above
def main(value1, value2):
    sum_variables(value1, value2)
    dif_variables(value1, value2)
    prod_variables(value1, value2)
    quot_variables(value1, value2)

# Call the main function and pass in the converted response values
main(number1, number2)
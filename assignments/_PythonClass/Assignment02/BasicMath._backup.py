# ----------------------------------------------- #
# Title: Basic Math Script
# Dev: KBiondich 
# Desc: Script that captures two numbers from the user, performs calculations on those numbers, and returns the results of the calculations.
# Changelog: (who, when, what)
# 	kbiondich,7/14/23,Created File
# ------------------------------------------------#

## Get user input
def capture_responses(question):
    responses = []

    responses.append("Enter a first number: ")
    responses.append("Enter a second number: ")

    return responses

# Convert strings to a number data type

def convert_to_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

# Computem the sum of the two variables

def sum_values(values):

    sum_values = [].append(values)
    # add the values to each other with the addition opperand
    for i in sum_values:
        sum_results += sum_values[i]
            
    ## Print the result
    print(f'\nThe sum of {sum_values[0]} and {sum_values[1]} is: {sum_values}')

# Find the difference of the two inputs

def dif_result (values):

    # ## ensure the data types of the paraments are numbers

    # find the absolute value of the difference between the values
    dif_values = [].append(values)
    
    for i in dif_values:
        
        dif_results -= abs(dif_values[i])
        

    # print the result
    print(f"The difference between {dif_values[0]} and {dif_values[1]} is: {dif_results}")


# Find the product of the 2 inputs

def prod_result (values):

    # ## ensure the data types of the paraments are numbers

    # find the product of string1 * string2
    prod_value = [].append(values)

    # Print the result
    print(f"The product of {prod1} times {prod2} is: {prod_value}")


# Find the quotient of the 2 inputs
def quot_result (quot1, quot2):

    # ## ensure the data types of the paraments are numbers

    # find the quotient of string1 divided by string2
    quot_value = float(quot1 / quot2)

    #Print the result
    print(f"The quotient of {quot_string1} divided by {quot_string2} is: {quot_value}")
    return (quot_string1, quot_string2)

# Define the starting point of the script

def main():
    
    captured_inputs = []
    
    captured_inputs[0] = input("Enter a first number: ")
    captured_inputs[1] = input("Enter second number: ")

    
    sum_result( )
    dif_result( )
    prod_result()
    quot_result()

main(string1, string2)
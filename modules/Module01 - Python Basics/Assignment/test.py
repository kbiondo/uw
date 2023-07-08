# ----------------------------------------------- #
# Assignment #1 - A simple script to capture user first name and last name and print it back to the user
# These first few lines are comments indicated by the 'pound' character 

# The following lines are python statements that python will execute one at a time (line by line)

# The first statement will create a function which will contain a group of statements
# Indentation is used define a group of statements that reside inside the function
def captureUserName():

	# This next statement will invoke the print function and will print to the terminal
	print("Please enter your name")

	'''
	This is a block comment (indicated by the triple quotes)

	These next statements create variables to hold the text values that the 
	input functions will capture from the terminal prompt, typed by the user
	'''
	firstName = input("First Name: ")
	lastName = input("Last Name: ")

	# This statement will print the text "You Entered: " and the values of the variables in a concatenated output
	print("You entered: ", firstName,"", lastName)

	# This last statement is used to provide a pause at the end of the file so the user can read the previous output
	input("\n\nPress the enter key to exit.")

captureUserName()
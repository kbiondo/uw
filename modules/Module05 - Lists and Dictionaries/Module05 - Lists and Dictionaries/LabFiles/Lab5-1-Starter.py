# -------------------------------------------------- #
# Title: Lab 5-1
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Your Name Here>,<Date>, Added read/write to file code
# -------------------------------------------------- #

# Declare my variables
strChoice = '' # User input
lstRow = []  # list of data
strFile = 'HomeInventory.txt'  # data storage file
objFile = None  # file handle

# Get user Input
while(True):
    print("Write or Read file data, then type 'Exit' to quit!")
    strChoice = input("Choose to [W]rite or [R]ead data: ")

    # Process the data
    if (strChoice.lower() == 'exit'): break
    elif (strChoice.lower() == 'w'):
        # List to File
        print('ToDo: add code here')
    elif (strChoice.lower() == 'r'):
        # File to List
        print('ToDo: add code here')
    else:
        print('Please choose either W or R!')

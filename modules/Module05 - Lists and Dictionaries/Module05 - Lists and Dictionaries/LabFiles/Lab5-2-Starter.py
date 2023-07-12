# -------------------------------------------------- #
# Title: Listing 9
# Description: Writing and Reading Data from a file
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Your Name Here>,<Date>,Changed rows from lists to dictionaries
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
        objFile = open(strFile, "w")
        lstRow = ["Lamp", "$30"]
        objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
        lstRow = ["End Table", "$60"]
        objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
        objFile.close()
    elif (strChoice.lower() == 'r'):
        # File to List
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",") # Returns a list!
            print(lstRow[0] + '|' + lstRow[1].strip())
        objFile.close()
    else:
        print('Please choose either W or R!')

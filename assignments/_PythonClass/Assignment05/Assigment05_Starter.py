# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KBiondich,8-5-23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstData = []    # A list that holds the extracted task name from the txt file
count = 0       # A counting variable

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# create a temp variable 'readFile' and pass objFile to it, create the file if it doesn't exist using the append argument, then the read argument
readFile = open(objFile, "a")
readFile = open(objFile, "r")
# use a for loop to loop through the file and do something with the things that are between the commas
for row in readFile:
    lstData = row.split(",")
    dicRow = {"Task":lstData[0],"Priority":lstData[1].strip()}
    lstTable.append(dicRow)


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority ")
        for i in lstTable:
            taskN = i["Task"]
            taskP = i["Priority"]
            print(str(taskN) + " | " + taskP)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        taskName = input("Task description: ")
        taskPriority = input("Task Priority (1 - 5): ")
        dicRow = {"Task":taskName,"Priority":taskPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    # this step displays to the user each task and asks for which to remove and then finds the one the user specifies
    elif (strChoice.strip() == '3'):
        print("# | Task | Priority")
        for i in lstTable:
            count += 1
            taskN = i["Task"]
            taskP = i["Priority"]
            print(str(count) + " | " + str(taskN) + " | " + taskP)
        delRow = input("Choose which to delete: ")
        lstTable.pop(int(delRow)-1)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        readFile = open(objFile, "w")
        for i in lstTable:
            readFile.write(i["Task"] + "," + i["Priority"] + '\n')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        readFile.close
        break  # and Exit the program

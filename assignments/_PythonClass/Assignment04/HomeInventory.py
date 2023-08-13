# ----------------------------------------------- #
# Title: Home Inventory Loop Funs
# Dev: KBiondich 
# Desc: A script that captures a household item, its estimated value and displays as a table with menu options
# Changelog: (who, when, what)
# 	kbiondich,7/30/23,Created File
# ------------------------------------------------#

# ------------------------------------------------#
# pseudo funs:
    # Step 1
    # Display a menu of choices to the user 
    # ("Add Data to List", "Display Current Data", "Exit and Save to File") 
# ------------------------------------------------#
# store the list of menu items in a list 
menuItems = ["Add Data to List", "Display Current Data", "Exit and Save to File"]
objFile = open("HouseInventory.txt","a")
householdItems = []
# Wrap everything in a while loop so the user returns to the menu after each selected action
while(True):
    # present the user a menu to choose what to do

    # Begin priting the menu: Tell the user what to do
    print("\nEnter Q to quit at any time")
    print("Select an Option: \n")

    # use a for loop to loop through the menuItems list
    for i in menuItems:
        # for formatting purposes, grab the position of i in the list and add 1 to it
        index = menuItems.index(i) + 1
        # convert index to a string for the print function
        stringIndex = str(index)
        # print the position of i along with the stored value in the menuItems list at that position
        print(stringIndex + ") " + i)

    # capture the user choice
    userChoice = input()
    # store items in a list


    if(userChoice.lower() == "q"): break
    # pseudo funs:
        # Step 2
        # Add a new item to the List(Table) each time the user makes that choice
    
    
    elif userChoice == "1":
        # open a saved file of the inventory list and append input to the bottom of the file
        while(True):
            print("Enter 'back' to return to the menu \n")
            houseItem = input("Enter a Household Item to the list: ")
            if(houseItem.lower() == "q"): break
            elif(houseItem.lower() == "back"): break
            else: 
                houseItemValue = input("Enter a Value for that Item to the list: ")
                if(houseItemValue.lower() == "q"): break
                elif(houseItemValue.lower() == "back"): break
                else: 
                    item = houseItem + " | " + houseItemValue
                    householdItems.append(item)
                    print("\nItem Added: " + houseItem + "|" + houseItemValue)
    
    # pseudo funs:
        # Step 3
        # Display the data in the List(Table) each time the user makes that choice
    elif userChoice == "2":
        print("\nCurrent Values:")
        print("Item | Value")
        for items in householdItems:
            print(items)

    # pseudo funs:
        # Step 4
        # Exit the program and save the data to a text file when the user makes that choice
    elif userChoice == "3":
        objFile.write("Item  |  Value \n")
        objFile.write("======================================== \n")
        for items in householdItems:
            objFile.write(items + "\n")
        objFile.close()
        break
# ----------------------------------------------- #
# Title: Home Inventory Loop Funs
# Dev: KBiondich 
# Desc: A script that captures a household item, its estimated value and displays as a table with menu options
# Changelog: (who, when, what)
# 	kbiondich,7/30/23,Created File
# ------------------------------------------------#

# pseudo funs:
# Step 1
# Display a menu of choices to the user 
# ("Add Data to List", "Display Current Data", "Exit and Save to File") 

# store the list of menu items in a list
menuItems = ["Add Data to List", "Display Current Data", "Exit and Save to File"]

# Tell the user what to do
print("Select an Option: ")

# use a for loop to loop through the menuItems list
for i in menuItems:
    # for formatting purposes, grab the position of i in the list and add 1 to it
    index = menuItems.index(i) + 1
    # print the position of i along with the stored value in the menuItems list at that position
    print(index + ") " + i)

")

# Step 2
# Add a new item to the List(Table) each time the user makes that choice

# Step 3
# Display the data in the List(Table) each time the user makes that choice

# Step 4
# Exit the program and save the data to a text file when the user makes that choice

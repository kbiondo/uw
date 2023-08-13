# ----------------------------------------------- #
# Title: Home Inventory Script
# Dev: KBiondich 
# Desc: A script that captures a household item, its estimated value and stores it in a txt file
# Changelog: (who, when, what)
# 	kbiondich,7/22/23,Created File
# ------------------------------------------------#

# pseudo-funs
# Get user input
# Save the input to a file
# Display the results

# Create an object and call the open function and pass the "a" argument to indicate appending information to the file
objFile = open("Inventory.txt", "a")

# Inform the user how to exit the while loop 
print("Type in a string to write (Enter 'Exit' to quit!)")

# Begin a while loop that captures user input, checks for the exit condition, 
# and writes the info to the file if the condition evaluates to false 
while(True):
  houseItem = input("Enter a household item: ")
  if(houseItem.lower() == "exit"): break
  itemValue = input(f"Enter {houseItem} value: ")
  if(itemValue.lower() == "exit"): break
  else: objFile.write("Item: " + houseItem + " Value: " + itemValue + "\n")
objFile.close()

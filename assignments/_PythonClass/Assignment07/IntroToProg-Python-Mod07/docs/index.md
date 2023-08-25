<<<<<<< HEAD
## IntroToProg-Python-Mod07 - Assignment06 Website 

Made a quick website from a gitlab repo. 
=======
# Pickling With Errors
## Introduction
<<<<<<< HEAD
In this weeks episode, we learn about pickling and all the fun around error handling.
### Subtopic
## Summary
>>>>>>> cdcfec42c09f81d78d6c8c31ce222ecc213d91cf
=======
In this weeks episode, we learn about pickling and all the fun around error handling. Week 7 of the course introduced pickling and error handling in python. The following paragraphs outline the examples I found on the internet and the methods that were used to create a game save state into a state.bin file as well as how the try, exception, and finally error handling block statements work. 
## Intended Outcome
The intended outcome of this week is the example of pickling game save states and error handling. 

  ![Intended Outcome](https://github.com/kbiondo/IntroToProg-Python-Mod07/blob/main/docs/images/07figure1.png?raw=true "Intended Outcome")
## Learning to Pickle
After a quick googling, I stumbled upon this website (The ultimate guide to Python pickle, n.d.). I used its example of how to pickle a game save state to a saveState.bin file, and then read that file back into the script. I chose this site because it appeared to have a short and easy example that I could use. I unfortunately ran into some issues with it and ended up having to use some of the try, except handling from the second part of the script. Technically my script runs fine, but it could use some work with the ‘EndOFFIle’ issue it seems to be creating. I’ll have to continue researching. 
Initially, this example creates a class of GameItem and a second class of GameState. It gives a player, an obstacle, and items an initial state and then passes those to a state variable. From there, a saveState variable is created to hold the open function and an argument of ‘wb’ write binary is passed to it. Then pickle.dump reads the state object into a ‘saveState’ binary file.
Next, saveState is passed the open function with an argument of ‘rb’ read binary and the saveState.bin file is opened and passed into savedState. From here I get an EOFError and use the try and except handling to either open and read the file contents or to use the previous values of state. 
I need to do a little more research on why the EOF error is occurring.

```
# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickling and error handling
# ChangeLog (Who,When,What):
# KBiondich,8-18-2023,Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #



# learning how to pickle
# From: https://snyk.io/blog/guide-to-python-pickle/
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
# The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
# The process of converting a python object into a character stream is called pickling or serialization.
# The reverse process is called unpickling or deserialization.

import pickle

# To pickle a file into an object:

# This example from snyk creates an example game that dumps the state of the game into a file called state.bin
class GameItem:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

# this is an example of how a game might save a play state
class GameState:
    def __init__(self, player_coordinates, obstacles, items):
        self.player_coordinates = player_coordinates
        self.obstacles = obstacles
        self.items = items

# Constructing a specifc state and pickling it into an object:
player_coordinates = (3, 2)
obstacles = { (1, 1), (5, 6), (7, 4), (0, -1) }
items = [ GameItem("Sword", 500), GameItem("Potion", 150) ]

 # "wb" because we want to write in binary mode
state = GameState(player_coordinates, obstacles, items)
saveState = open("saveState.bin", "wb")
pickle.dump(state, saveState)

# To unpickle a file into an object:
# "rb" because we want to read in binary mode
savedState = open("saveState.bin", "rb") 
try:
    state = pickle.load(savedState)
except EOFError:
    print("End of file error")
    state = GameState(player_coordinates, obstacles, items)

print("Player coordinates:", state.player_coordinates)
print("Obstacles:", state.obstacles)
print("Number of items:", len(state.items))
```

## Learning to Handle Errors
I then googled a few sites about handling errors and came across this website (Python Exception Handling, n.d.). The example creates a three element list of numbers and then starts a try block and attempts to find an element at position 4. The except portion of the try block catches the error and explains that issue. Another example is the divide by zero error. This try block presents x = 10/0 and catches the error with the ‘ZeroDivisionError’ exception. This example also uses a ‘Finally’ block which executes regardless of the exceptions above.

```
# ---------------------------------------------------------------------------- #
# Learning how to do error handling
# From: https://www.geeksforgeeks.org/python-exception-handling/
# this site explains some of the types of error handling that is built into python and how to use them effectively.

# Simple error to handle runtime issues
a = [1, 2, 3]
try:
    print('remember, this list is %d elements long' %(len(a)))
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array. Position 3 is actually the 4th element.
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("uh oh, you chose a 4th element")


# another error example but with using of the finally exception clause:
 
# No exception Exception raised in try block
try:
    x = 10/0
    print(x)
 
#this handles the divide by zero exception
except ZeroDivisionError:
    print("no no divide by zero = bad")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('Finally is always executed even if you try to divide by zero, which is bad')
```

## Observations
This week’s objective was interesting. Pickling can be a useful resource for saving obscured data which I may use at work. Although I haven’t quite figured out how to solve the End OF File error, I see this as a useful exercise. The error handling portion of the objective is also useful to understand, especially as I build applications for work. Another big understanding is the vast amount of examples around the web. I found that I could google and find examples for everything I was trying to accomplish. 
## References
  Python Exception Handling. (n.d.). Retrieved from Geeks for Geeks: https://www.geeksforgeeks.org/python-exception-handling/  
  
  The ultimate guide to Python pickle. (n.d.). Retrieved from snyk.io: https://snyk.io/blog/guide-to-python-pickle/


>>>>>>> 273040dffd08c6cae00572983cfc2ea77df6ee0f

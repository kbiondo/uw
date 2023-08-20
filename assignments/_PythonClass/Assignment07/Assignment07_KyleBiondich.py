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
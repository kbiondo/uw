# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with classes in a module,
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

# This example from snyk creates an example game
class GameItem:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class GameState:
    def __init__(self, player_coordinates, obstacles, items):
        self.player_coordinates = player_coordinates
        self.obstacles = obstacles
        self.items = items

# Constructing a specifc state and pickling it into an object:
player = (3, 2)
obstacles = { (1, 1), (5, 6), (7, 4), (0, -1) }
items = [ GameItem("Sword", 500), GameItem("Potion", 150) ]

state = GameState(player, obstacles, items)
with open("state.bin", "wb") as f: # "wb" because we want to write in binary mode
    pickle.dump(state, f)

# To unpickle a file into an object:
with open("state.bin", "rb") as f: # "rb" because we want to read in binary mode
    state = pickle.load(f)

print("Player coordinates:", state.player)
print("Obstacles:", state.obstacles)
print("Number of items:", len(state.items))

# ---------------------------------------------------------------------------- #
# Learning how to do error handling
# From: https://www.geeksforgeeks.org/python-exception-handling/


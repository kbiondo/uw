# ------------------------------------------------- #
# Title: Lab 8-3
# Description: A class with attributes
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

class Person(object):
    # --Fields--
    # first_name_str = ""  <- Delete this. Python does not use fields for instance data

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # Attributes
        self.first_name_str = first_name
        self.last_name_str = last_name

# --End of class--

# --- Use the class ----
objP1 = Person("Bob", 123)
print(objP1.first_name_str, objP1.last_name_str)
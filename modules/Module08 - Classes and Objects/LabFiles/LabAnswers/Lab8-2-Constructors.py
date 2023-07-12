# ------------------------------------------------- #
# Title: Lab 8-2
# Description: A class with a constructor
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# --- Make the class ---
class Person(object):
    # --Fields--
    strFirstName = ""
    strLastName = ""

    # -- Constructor --
    def __init__(self, first_name, last_name):
        self.strFirstName = first_name
        self.strLastName = last_name
# --End of class--

# --- Use the class ----
objP1 = Person("Bob", "Smith")
print(objP1.strFirstName, objP1.strLastName)

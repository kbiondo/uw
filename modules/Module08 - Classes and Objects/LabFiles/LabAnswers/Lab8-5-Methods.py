# ------------------------------------------------- #
# Title: Lab 8-5
# Description: A class with methods
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# --- Make the class ---
class Person(object):

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # 	   -- Attributes --
        self.first_name = first_name
        self.last_name = last_name

    # -- Properties --
    # first_name
    @property  # DON'T USE NAME for this directive!
    def first_name(self): # (getter or accessor)
        return str(self.__first_name).title()  # Title case

    @first_name.setter  # The NAME MUST MATCH the property's!
    def first_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    # last_name
    @property  # DON'T USE NAME for this directive!
    def last_name(self):  # (getter or accessor)
        return str(self.__last_name).title()  # Title case

    @last_name.setter  # The NAME MUST MATCH the property's!
    def last_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        return self.first_name + ',' + self.last_name

    def __str__(self):
        return self.to_string()

# --End of class--

# --- Use the class ----
objP1 = Person("bob", "123")
print(objP1)


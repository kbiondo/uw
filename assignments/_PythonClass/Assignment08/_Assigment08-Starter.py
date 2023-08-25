# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# KBiondich,8-25-23,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        K.Biondich,8-25-23,Modified code to complete assignment 8
    """
    # TODO: Add Code for Product class (Constructor, Properties, & Methods)
    # Constructor
    def __init__(self, product_name, product_price):
        self.__product_name = product_name
        self.__product_price = product_price

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value): 
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Product prices must be numbers")

    # Methods
    def to_string(self):
        ''' Returns object data as a string 
            Product Name + Product Price
        '''
        object_data = self.__product_name + ',' + str(self.__product_price)
        return object_data

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        K.Biondich,8-25-23,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        ''' Reads data from a file into a list of objects

        :param file_name: (string) with name of file:
        :return: (list) of Product Class objects
        '''
        list_of_product_objects = []
        file_obj = open(file_name, "a")
        file_obj = open(file_name, "r")
        for row in file_obj:
            file_data = row.split(",")
            product = Product(file_data[0].strip(),file_data[1].strip())
            list_of_product_objects.append(product)
        return list_of_product_objects

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_objects):
        ''' Writes data from a list of objects to a file

        :param file_name: (string) with name of file:
        :param list_of_objects: (list) of objects:
        :return: nothing
        '''
        file = open(file_name, 'w')
        for row in list_of_objects:
            file.write(row.to_string() + '\n')
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """  A class for performing Input and Output
    methods:
        print_menu_items():
        print_current_list_items(list_of_product_objects):
        input_product_data():
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        K.Biondich,8-25-23,Modified code to complete assignment 8
    """
    # Add code to show menu to user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks in the terminal window

    # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
        ''' Gets the menu choice from a user
        :return: string
        '''
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks in the terminal window
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def print_current_list_items(list_of_objects):
        ''' Shows the current items in the list of objects
        :param list_of_objects: (list) of objects:
        :return: nothing
        '''
        print("******* The current items in the list are: *******")
        for row in list_of_objects:
            print(row.product_name + ' (' + str(row.product_price) + ')')
        print("*******************************************")
        print()  # Add an extra line for looks in the terminal window
        
    # TODO: Add code to get product data from user
    @staticmethod
    def input_product_data():
        ''' Gets data for a product object
        :return: (object) product
        '''
        try:
            name = str(input("What is the product name? - ")).strip()
            price = float(input("What is the product price? - "))
            print()  # Add an extra line for looks in the terminal window
            newproduct = Product(product_name=name, product_price=price)
        except Exception as e:
            print(e)
        return newproduct

# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
# Show user a menu of options
while True:
# Show user a menu of options
    IO.print_menu_items()
# Get user's menu option choice
    strChoice = IO.input_menu_choice()
    # Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.print_current_list_items(lstOfProductObjects)
        continue
    # Let user add data to the list of product objects
    elif strChoice.strip() == '2':
        lstOfProductObjects.append(IO.input_product_data())
        continue
    # let user save current data to file and exit program
    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue
    # Let user exit program
    elif strChoice.strip() == '4':
        break
    else:
        print('Please enter a number between 1 and 4')
        continue

# Main Body of Script  ---------------------------------------------------- #


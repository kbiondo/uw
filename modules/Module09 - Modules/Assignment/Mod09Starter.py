# ------------------------------------------------------------------------------------ #
# Title: Module 09 Starter Code
# Description: This is the code you will divide into multiple code modules
# ChangeLog (Who,When,What):
# RRoot, 1.1.2030, Created started script
# TODO: Move all this code into separate modules
# ------------------------------------------------------------------------------------ #

# Data Layer
class Person(object):  # Inherits from object
    """Stores data about a persons:

    properties:
        first_name: (string) with the person's first name

        last_name: (string) with the person's last name
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # -- Attributes are now managed by the properties --
        self.first_name = first_name
        self.last_name = last_name

    # -- Properties --
    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data """
        return self.__str__()

    def __str__(self):
        """ Implicitly returns a string with this object's data """
        return self.first_name + ',' + self.last_name

class Employee(Person):  # Inherits from Person
    """Stores data about an Employee:

    properties:
        employee_id: (int) with the employee's ID

        first_name: (string) with the employee's first name

        last_name: (string) with the employee's last name
    methods:
        to_string() returns comma separated product data (alias for __str__())
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    def __init__(self, employee_id, first_name, last_name):
        # Attributes
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    # --Properties--
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if str(value).isnumeric():
            self.__employee_id = value
        else:
            raise Exception("IDs must be numbers")

    # --Methods--
    def to_string(self):  # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ',' + data

    def __str__(self):  # Overrides the original method (polymorphic)
        """ Implicitly returns field data """
        data = super().__str__()  # get data from parent(super) class
        return str(self.employee_id) + ',' + data
    # --End of Class --

# Processing Layer
class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row.__str__() + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                row = line.split(",")
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows


# Presentation Layer
class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
    """
    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data.
        3) Remove employee data.
        4) Save employee data to File
        5) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The current items employees are: *******")
        for row in list_of_rows:
            print(str(row.employee_id)
                  + ","
                  + row.first_name
                  + ","
                  + row.last_name)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_employee_data():
        """ Gets data for a employee object

        :return: (employee) object with input data
        """
        emp = None
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - ").strip())
            print()  # Add an extra line for looks
            emp = Employee(employee_id, first_name, last_name)
        except Exception as e:
            print(e)
        return emp

    @staticmethod
    def input_employee_id():
        msg = "Which Employeed Data do you what to delete (Provide the ID) "
        id_str = input(msg)
        return id_str


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
# Data #
lstEmployeeTable = []  # A list/table of Employee objects
lstFileData = []  # A list/table of string objects in a list


# Load data from file into a list of employee objects when script starts
lstFileData = FileProcessor.read_data_from_file("EmployeeData.txt")

for row in lstFileData:
    lstEmployeeTable.append(Employee(row[0], row[1], row[2].strip()))

EmployeeIO.print_current_list_items(lstEmployeeTable)

# Show user a menu of options
while True:
    EmployeeIO.print_menu_items()
    # Get user's menu option choice
    strOption = EmployeeIO.input_menu_options()
    if strOption == "1":
        # Show user current data in the list of employee objects
        EmployeeIO.print_current_list_items(lstEmployeeTable)
        continue
    elif strOption == "2":
        # Let user add data to the list of employee objects
        lstEmployeeTable.append(EmployeeIO.input_employee_data())
        EmployeeIO.print_current_list_items(lstEmployeeTable)
        continue
    elif strOption == "3":
        # let user save current data to file
        id_to_remove = EmployeeIO.input_employee_id()
        for row in lstEmployeeTable:
            if str(row.employee_id) == id_to_remove:
                lstEmployeeTable.remove(row)
        EmployeeIO.print_current_list_items(lstEmployeeTable)
        continue
    elif strOption == "4":
        # let user save current data to file
        FileProcessor.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
        print("Data Saved to File")
        continue
    elif strOption == "5":
        # exit program
        break
    else:
        print("Please enter only 1, 2, 3, 4, or 5")
# Main Body of Script  ---------------------------------------------------- #

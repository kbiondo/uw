# ------------------------------------------------- #
# Title: Lab08-1-Fields
# Description: A simple example of a class field
# ChangeLog: (Who, When, What)
# RRoot,1.1.2030,Created Script
# ------------------------------------------------- #

# --- Make the class ---
import os.path

class FileInfo:
    # --Fields--
    FILE_FOLDER = os.getcwd()  # Python's get the current working directory function
    FILE_NAME = 'program_data.txt'
    FULL_PATH = FILE_FOLDER + '/' + FILE_NAME
# End of class

# --- Use the class ----
try:
    print('Reading data from', FileInfo.FULL_PATH)
    file_obj = open(FileInfo.FULL_PATH, 'r')
except FileNotFoundError as e:
    error_msg = ' The data file cannot be found.\n'
    error_msg += ' Please check that the ' + FileInfo.FILE_NAME
    error_msg += ' file exists in the ' + FileInfo.FILE_FOLDER
    print(error_msg)



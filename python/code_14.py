# Write a python program showing practical example of absolute path

import os

def absolute_file_path(path_fname):
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("phonebook.txt"))


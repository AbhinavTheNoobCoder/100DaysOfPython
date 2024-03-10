#DAY 68 of Python - Exercise 7
#Clear the clutter
import os

def clutter_extension(directory, extension):
    os.chdir(directory)
    num = 1
    for file in os.listdir(directory):
        if extension in file:
            os.rename(file, f"{num}{extension}")
            num += 1

directory = input("Enter directory where you want to change the file names: ")
extension_name = input("Enter extension whose files are to be renamed with numbers: ")
clutter_extension(directory, extension_name)
print("Check your directory to notice the changes made!")
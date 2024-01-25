#DAYS 44, 45, 46 - import, use of __name__ == "__main__" and os module
import os
def CreateDirectory(directory):
    os.mkdir(directory)
    print("Directory created.")
def ListingDirectory(directory):
    folders = os.listdir(directory)
    print(f"List of folders in the directory - {folders}")
def RenameFile(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"File {old_name} renamed to {new_name}")
def DeleteFile(filename):
    os.remove(filename)
    print(f"File - {filename} has been removed.")

def main():
    while True:
        choice = int(input('''Welcome to your Files Manager.
What would you like to do? Press -
1 for Creating a Directory
2 for Listing Folders in a Directory
3 for Renaming a File
4 for Deleting a File
5 to Quit
>>> '''))
        if choice == 1:
            directory_name = input("Enter directory to be created: ")
            CreateDirectory(directory_name)
        elif choice == 2:
            directory_name = input("Enter directory to be listed: ")
            ListingDirectory(directory_name)
        elif choice == 3:
            original = input("Enter original name: ")
            renamed = input("Enter new name: ")
            RenameFile(original, renamed)
        elif choice == 4:
            name = input("Enter file to be deleted: ")
            DeleteFile(name)
        elif choice == 5:
            break
        print("")

if __name__ == "__main__":
    main()
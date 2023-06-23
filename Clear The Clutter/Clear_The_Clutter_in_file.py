import os
import os.path
import shutil


# Function to count total no. of files of given file type
def countFiles(extension):
    noOfFiles = 0
    for file in files:
        if file.endswith(extension):
            noOfFiles += 1
    print(f"There are {noOfFiles} files of type {extension}")


# Function to display files of specific file type in the given directory


def displaySpecificFiles(extension, files):
    print(f"Displaying all the {extension} files in '{filePath}' directory")
    countFiles(extension)

    for file in files:
        if file.endswith(extension):
            print(file)


# Function to display all the files in the given directory
def displayAllFiles(files):
    print(f"Displaying all files in the '{filePath}' directory")
    print(f"No. of Files (including folders) = {len(files)}")

    for file in files:
        print(file)


# Function to rename files of Specific Types
def renameFiles(path, files, extension):
    print(f"Renaming all the {extension} files in the given folder")
    countFiles(extension)

    i = 1
    for file in files:
        exist = f"{path}/{i}{extension}"
        if (os.path.exists(exist)):
            i = i+1
        else:
            if file.endswith(extension):
                os.rename(f"{path}/{file}", f"{path}/{i}{extension}")
                i = i+1


# Function to delete files of specific file type
def deleteSpecificFile(path, files, extension):
    print(f"Deleting all the {extension} files from '{path}' directory")
    countFiles(extension)

    for file in files:
        if file.endswith(extension):
            filePath = f"{path}/{file}"
            os.remove(filePath)


# Function to delete all the files in current directory
def deleteAllFiles(path):
    print(f"Deleting all files from '{filePath}' directory")
    shutil.rmtree(path)


# ---------------------------------------------------------------------------------------------
# Driver Code
filePath = input("Enter the absolute file path : ")

# List of all the Files (including Folders)
files = os.listdir(filePath)

while True:

    print()
    print("*** Operations to perform: ***".center(30))
    print("1. Display file(s) of specific file type")
    print("2. Display all files")
    print("3. Rename file(s) of same type")
    print("4. Delete file(s) of specific file type")
    print("5. Delete all files")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    # Using Match Case for processing user input
    match choice:
        case 1:
            print()
            extension = input(
                "Enter the file type ( extension including '.' ) : ")

            displaySpecificFiles(extension, files)

        case 2:
            print()
            displayAllFiles(files)

        case 3:
            print()
            extension = input(
                "Enter the file type ( extension including '.' ) : ")

            renameFiles(filePath, files, extension)

        case 4:
            print()
            extension = input(
                "Enter the file type ( extension including '.' ) : ")

            deleteSpecificFile(filePath, files, extension)

        case 5:
            print()
            deleteAllFiles(filePath)

        case 6:
            break

        # Default Case
        case _:
            print("Invalid choice")

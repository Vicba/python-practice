import os
import shutil
from datetime import datetime
from pathlib import Path


def list_files():
    """ 
        List all files in the current working directory. 
    """

    files = os.listdir()
    print("\nFiles and Directories in the current working directory:")
    for file in files:
        path = os.path.join(os.getcwd(), file) # getcwd() returns current working directory of a process.
        size = os.path.getsize(path)
        modified_time = datetime.fromtimestamp(os.path.getmtime(path))
        print(f"{file}\t Size: {size} bytes\t Last Modified: {modified_time}")
    print()


def list_files_dir():
    """ 
        List all files in the current working directory. 
    """

    dir_name = input("Enter the name of the directory to list files: ")
    files = os.listdir(dir_name)
    if len(files) == 0:
        print("No files found in the current directory.\n")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)

        print()

############################### CREATE ##########################################

def create_file():
    """ 
        Create a new file in the current working directory. 
    """

    file_name = input("Enter the name of the file to create: ")
    content = input("Enter the content of the file: ")
    with open(file_name, 'w') as file:
        file.write(content)

    print(f"File '{file_name}' created successfully!\n")
    

def create_directory():
    """
        Create a new directory in the current working directory.
    """

    dir_name = input("Enter the name of the directory: ")
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created successfully!\n")

############################### READ ##########################################
    
def read_file():
    """ 
        Read a file in the current working directory. 
    """

    file_name = input("Enter the name of the file to read: ")
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.\n")

############################### UPDATE ##########################################

def update_file():
    """ 
        Update a file in the current working directory. 
    """

    file_name = input("Enter the name of the file to update: ")
    content = input("Enter the content to append: ")
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print(f"File '{file_name}' updated successfully!\n")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.\n")


############################### DELETE ##########################################

def delete_file():
    """ 
        Delete a file in the current working directory. 
    """

    file_name = input("Enter the name of the Directory you want to delete: ")
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully!\n")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.\n")

def delete_directory():
    """ 
        Delete a directory in the current working directory. 
    """

    dir_name = input("Enter the name of the directory to delete: ")
    try:
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' deleted successfully!\n")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found.\n")


def main():
    while True:
        print("1. List Files")
        print("2. List files of directory")
        print("3. Create File")
        print("4. Create Directory")        
        print("5. Read file")
        print("6. Update file")
        print("7. Delete file")
        print("8. Delete directory")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            list_files()
        elif choice == '2':
            list_files_dir()
        elif choice == '3':
            create_file()
        elif choice == '4':
            create_directory()
        elif choice == '5':
            read_file()
        elif choice == '6':
            update_file()
        elif choice == '7':
            delete_file()
        elif choice == '8':
            delete_directory()
        elif choice == '9':
            print("Exiting the program. Goodbye! \n")
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
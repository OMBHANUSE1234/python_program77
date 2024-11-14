import os

ch = int(input("Enter your choice: \n1. Create Directory\n2. List Files\n3. Rename Directory\n4. Exit\n"))

if ch == 1:
    # Create a directory
    name = input("Enter the name of the directory to create: ")
    try:
        os.mkdir(name)
        print(f"Directory '{name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

elif ch == 2:

    path = input("Enter the directory path to list files (e.g., 'Python' or '.'): ")
    try:
        files = os.listdir(path)
        print("Files in directory:", files)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

elif ch == 3:
    # Rename a directory
    old_name = input("Enter the current directory name: ")
    new_name = input("Enter the new directory name: ")
    try:
        os.rename(old_name, new_name)
        print(f"Directory renamed from '{old_name}' to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"Directory '{old_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

elif ch == 4:
    # Exit the program
    print("Exiting the program.")
else:
    print("Invalid choice. Please enter a number between 1 and 4.")

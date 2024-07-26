import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.connection import login

def main():
    print("Welcome to the Instagram CLI")
    print("1. Login")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter your Instagram username: ")
        password = input("Enter your Instagram password: ")
        if login(username, password):
            print("You are now logged in.")
        else:
            print("Login failed.")
    elif choice == '2':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


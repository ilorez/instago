import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.connection import login
from Account import Account

def main():
    account_manager = Account()

    while True:
        print("\nMenu:")
        print("1. Login with an account")
        print("2. Add an account")
        print("3. Update an account")
        print("4. Delete an account")
        print("5. Delete all accounts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            accounts = account_manager.get_accounts()
            if not accounts:
                print("No accounts found. Please add an account first.")
            else:
                print("Select an account to use:")
                for i, account in enumerate(accounts):
                    print(f"{i + 1}: {account['username']}")
                print("0: Back to main menu")

                account_choice = input("Enter your choice: ")
                if account_choice == '0':
                    continue

                try:
                    account_choice = int(account_choice)
                    if 1 <= account_choice <= len(accounts):
                        selected_account = accounts[account_choice - 1]
                        username = selected_account['username']
                        password = selected_account['password']
                        if login(username, password):
                            print("You are now logged in.")
                        else:
                            print("Login failed.")
                    else:
                        print("Invalid choice. Please select a valid option.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '2':
            username = input("Enter the new Instagram username: ")
            password = input("Enter the new Instagram password: ")
            account_manager.add_account(username, password)
            print("Account added successfully.")

        elif choice == '3':
            username = input("Enter the username of the account to update: ")
            new_password = input("Enter the new password: ")
            account_manager.update_account(username, new_password)
            print("Account updated successfully.")

        elif choice == '4':
            username = input("Enter the username of the account to delete: ")
            account_manager.delete_account(username)
            print("Account deleted successfully.")

        elif choice == '5':
            account_manager.delete_all_accounts()
            print("All accounts deleted successfully.")

        elif choice == '0':
            print("Exiting...")
            sys.exit()
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


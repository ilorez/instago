import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.connection import login
from Account import Account
from InquirerPy import inquirer

def main():
    account_manager = Account()

    while True:
        choice = inquirer.select(
            message="Menu:",
            choices=[
                "Login with an account",
                "Add an account",
                "Update an account",
                "Delete an account",
                "Delete all accounts",
                "Exit"
            ],
            vi_mode=True,
        ).execute()

        if choice == "Login with an account":
            accounts = account_manager.get_accounts()
            if not accounts:
                print("No accounts found. Please add an account first.")
            else:
                account_choices = [f"{account['username']}" for account in accounts]
                account_choices.append("Back to main menu")
                account_choice = inquirer.select(
                    message="Select an account to use:",
                    choices=account_choices,
                    vi_mode=True,
                ).execute()

                if account_choice == "Back to main menu":
                    continue

                selected_account = next(acc for acc in accounts if acc['username'] == account_choice)
                username = selected_account['username']
                password = selected_account['password']
                if login(username, password):
                    print("You are now logged in.")
                else:
                    print("Login failed.")

        elif choice == "Add an account":
            username = inquirer.text(message="Enter the new Instagram username:", vi_mode=True).execute()
            password = inquirer.secret(message="Enter the new Instagram password:", vi_mode=True).execute()
            account_manager.add_account(username, password)
            print("Account added successfully.")

        elif choice == "Update an account":
            username = inquirer.text(message="Enter the username of the account to update:", vi_mode=True).execute()
            new_password = inquirer.secret(message="Enter the new password:", vi_mode=True).execute()
            account_manager.update_account(username, new_password)
            print("Account updated successfully.")

        elif choice == "Delete an account":
            username = inquirer.text(message="Enter the username of the account to delete:", vi_mode=True).execute()
            account_manager.delete_account(username)
            print("Account deleted successfully.")

        elif choice == "Delete all accounts":
            account_manager.delete_all_accounts()
            print("All accounts deleted successfully.")

        elif choice == "Exit":
            print("Exiting...")
            sys.exit()

if __name__ == "__main__":
    main()


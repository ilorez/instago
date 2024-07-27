import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.connection import login, get_driver
from Account import Account
from InquirerPy import inquirer
from lib.follow_user_followers import follow_user_followers

def actions_menu(driver):
    while True:
        choice = inquirer.select(
            message="Actions Menu:",
            choices=[
                "Follow user followers",
                "Follow user following",  # Placeholder for future functionality
                "Back to main menu"
            ],
            vi_mode=True
        ).execute()
        
        if choice == "Follow user followers":
            username = inquirer.text(message="Enter the username of the user:", vi_mode=True).execute()
            max_followers = inquirer.text(message="Enter the maximum number of followers to follow:", vi_mode=True).execute()
            follow_user_followers(username, int(max_followers), driver)
            print(f"Started following followers of {username}.")
            
        elif choice == "Back to main menu":
            break

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
                "Actions Menu",
                "Exit"
            ],
            vi_mode=True
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
                    vi_mode=True
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
        
        elif choice == "Actions Menu":
            if get_driver() is None:
                print("You need to login first.")
            else:
                actions_menu(get_driver())
                
        elif choice == "Exit":
            print("Exiting...")
            if get_driver():
                get_driver().quit()
            sys.exit()

if __name__ == "__main__":
    main()


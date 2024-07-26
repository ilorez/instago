import json
import os
from datetime import datetime

class Account:
    def __init__(self, file_path=None):
        if file_path is None:
            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Set the default file path to the same directory as main.py
            self.file_path = os.path.join(script_dir, 'accounts.json')
        else:
            self.file_path = file_path
        self._ensure_file()

    def _ensure_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def _load_accounts(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _save_accounts(self, accounts):
        with open(self.file_path, 'w') as file:
            json.dump(accounts, file, indent=4)

    def add_account(self, username, password):
        accounts = self._load_accounts()
        for account in accounts:
            if account['username'] == username:
                return  # Account already exists

        new_account = {
            'username': username,
            'password': password,
            'created_at': datetime.now().isoformat(),
            'times_used_count': 0
        }
        accounts.append(new_account)
        self._save_accounts(accounts)

    def update_account(self, username, new_password):
        accounts = self._load_accounts()
        for account in accounts:
            if account['username'] == username:
                account['password'] = new_password
                self._save_accounts(accounts)
                return
        print("Account not found.")

    def delete_account(self, username):
        accounts = self._load_accounts()
        accounts = [account for account in accounts if account['username'] != username]
        self._save_accounts(accounts)

    def delete_all_accounts(self):
        self._save_accounts([])

    def get_accounts(self):
        return self._load_accounts()


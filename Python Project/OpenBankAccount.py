# Bank Account Manager
class BankAccountsManager:
    def __init__(self):
        ## empty dictionary of accounts
        self.accounts = {}

    def add_account(self, account_holder, account_number, balance=0.0):
        ## new bank account to the dictionary
        if account_number not in self.accounts:
            self.accounts[account_number] = {
                'account_holder': account_holder,
                'balance': balance
            }
            print(f"Account {account_number} for {account_holder} added successfully.")
        else:
            print(f"Account number {account_number} already exists.")

    def delete_account(self, account_number):
        ## delete an account from the dictionary using its account number
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print(f"Account number {account_number} not found. No account deleted.")

    def update_account(self, account_number, **kwargs):
        ## update details of an account
        account = self.accounts.get(account_number)
        if account:
            account.update(kwargs)
            print(f"Account {account_number} updated successfully.")
        else:
            print(f"Account number {account_number} not found. No updates made.")

    def display_account_details(self, account_number):
        ## details of a specific account
        if account_number in self.accounts:
            account_details = self.accounts[account_number]
            print(f"Account Details for {account_number}:")
            for key, value in account_details.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print(f"Account number {account_number} not found.")


manager = BankAccountsManager()
# adding accounts
manager.add_account('Harry', '123456789', 1000)
manager.add_account('Alice', '987654321', 5000)

# updating an account
manager.update_account('123456789', balance=1100, account_holder='Harry')

# deleting an account
manager.delete_account('987654321')

# open account details
manager.display_account_details('123456789')

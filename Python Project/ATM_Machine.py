from datetime import datetime

class BankAccountsManager:
    def __init__(self):
        # empty dictionary of accounts
        self.accounts = {}

    def add_account(self, account_holder, account_number, balance=0.0):
        ## a new bank account 
        if account_number not in self.accounts:
            self.accounts[account_number] = {
                'account_holder': account_holder,
                'balance': balance,
                'transactions': []
            }
            self._add_transaction(account_number, 'Account opened', balance)
        else:
            print(f"Account number {account_number} already exists.")

    def _add_transaction(self, account_number, transaction_type, amount):
        # add transaction 
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.accounts[account_number]['transactions'].append(transaction)

    def deposit(self, account_number, amount):
        # deposite money into account
        if amount > 0:
            if account_number in self.accounts:
                self.accounts[account_number]['balance'] += amount
                self._add_transaction(account_number, 'Deposit', amount)
                print(f"Amount {amount} deposited successfully to account {account_number}.")
            else:
                print(f"Account number {account_number} not found.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, account_number, amount):
        # Withdraw money from the account
        if account_number in self.accounts:
            if 0 < amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                self._add_transaction(account_number, 'Withdrawal', amount)
                print(f"Amount {amount} withdrawn successfully from account {account_number}.")
            else:
                print("Insufficient balance or invalid withdrawal amount.")
        else:
            print(f"Account number {account_number} not found.")

    def display_account_details(self, account_number):
        # details of a specific account
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account Details for {account_number}:")
            for key in ['account_holder', 'balance']:
                print(f"{key.capitalize()}: {account[key]}")
            print("Transactions:")
            for transaction in account['transactions']:
                print(f"{transaction['date']}: {transaction['type']} of {transaction['amount']}")
        else:
            print(f"Account number {account_number} not found.")

    def delete_account(self, account_number):
        # delete an account from the dictionary using its account number
        if account_number in self.accounts:
            del self.accounts[account_number]
            print(f"Account {account_number} deleted successfully.")
        else:
            print(f"Account number {account_number} not found. No account deleted.")

manager = BankAccountsManager()
manager.add_account('Harry Thapa', '123456789', 1000)

# transactions
manager.deposit('123456789', 500)
manager.withdraw('123456789', 200)

# account details, including transactions
manager.display_account_details('123456789')

## Author : Hemant Thapa
## Date Push to Github: 27.02.2024

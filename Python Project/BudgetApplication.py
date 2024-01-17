#category class to manage financial transactions
class Category:
    def __init__(self, name):
        #initialise a category with a name and an empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        #add a deposit entry to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        #checking sufficient funds and add a withdrawal entry to the ledger
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        #return the current balance of the category
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount, other_category):
        #transfer funds to another category and record the transaction in both ledgers
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        #check if there are sufficient funds for a withdrawal
        return amount <= self.get_balance()

    def __str__(self):
        #generate a formatted string representation of the categorys ledger
        title = f"{self.name:-^30}\n"
        items = "".join(f"{entry['description'][:23]:23}{entry['amount']:7.2f}\n" for entry in self.ledger)
        total = sum(entry["amount"] for entry in self.ledger)
        output = title + items + "Total: " + f"{total:.2f}"
        return output

#Food category
food_category = Category("Food")
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")

#Clothing category
clothing_category = Category("Clothing")

#transfer funds from food to Clothing
food_category.transfer(50, clothing_category)

#print the ledger of food and Clothing categories
print(food_category)
print(clothing_category)

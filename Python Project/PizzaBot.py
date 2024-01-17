#importing random
import random

#class pizza bot
class PizzaBot:
    #initialise the PizzaBot object with default attributes
    def __init__(self):
        #bot name
        self.name = "Pizza Bot"
        #empty address
        self.address = ""
        #empty order list
        self.order = {"size": "", "toppings": [], "total": 0}
      
    #method to greet the customer
    def welcome(self):
        print("Welcome to Pizza Shop! You can call me {}.".format(self.name))
      
    #method to get customer information (name and address)
    def get_customer_info(self):
        name = input("What is your name? ").strip().capitalize()
        print(f"\nNice to meet you, {name}.")
        self.address = input("\nPlease enter your full address including postcode: ").strip()
      
    #method to choose the delivery method (delivery or collection)
    def choose_delivery_method(self):
        while True:
            print("\nDo you want delivery or collection?")
            print("Type 'DEL' for delivery and 'COL' for collection")
            del_col = input().strip().lower()
            #delivery options
            if del_col == "del":
                print(f"You have registered address for delivery as {self.address}.")
                break
            #collection options
            elif del_col == "col":
                print("You have selected the collection option. Address for collection is Glasgow, City Center.")
                break
            else:
                print("Invalid input. Please enter 'DEL' for delivery or 'COL' for collection.")

    #method to select the pizza size
    def select_pizza_size(self):
        sizes = {"S": 15, "M": 20, "L": 25}
        while True:
            print("\nWhat size of pizza do you want?")
            for size, price in sizes.items():
                print(f"{size} - {price} pounds")

            size = input("Choose a size (S, M, L): ").strip().upper()

            if size in sizes:
                self.order["size"] = size
                self.order["total"] += sizes[size]
                print(f"You have selected a {size} size pizza.")
                break
            else:
                print("Invalid size. Please choose S, M, or L.")
    #method to add toppings to the pizza
    def add_toppings(self):
        toppings = ["pepperoni", "mushrooms", "onions", "bell peppers", "olives"]
    
        while True:
            print("\nAvailable toppings: " + ', '.join(toppings))
            print("Would you like to add extra toppings to your pizza?")
            print("Type the name of the topping or 'DONE' to finish.")
            choice = input().strip().lower()
    
            if choice in toppings:
                self.order["toppings"].append(choice)
                self.order["total"] += 2
                toppings.remove(choice)  # Remove the chosen topping from the list
                print(f"Added {choice} topping to your pizza.")
            elif choice == "done":
                break
            else:
                print("Invalid input or topping not available.")

    #order summary and thank the customer
    def checkout(self):
        print(f"\nYour order summary:")
        print(f"Size: {self.order['size']}")
        if self.order["toppings"]:
            print("Toppings:", ', '.join(self.order["toppings"]))
        print(f"Total: £{self.order['total']}")
        print("\nThank you for your order!")
        print(f"{self.name} will deliver your pizza to {self.address}. Enjoy!")

    #method to run the pizza ordering process
    def run(self):
        #greet the customer
        self.welcome()  
        #customer information
        self.get_customer_info()  
        #delivery method
        self.choose_delivery_method()  
        #pizza size
        self.select_pizza_size()  
        #add toppings to the pizza
        self.add_toppings() 
        #order summary and thank the customer
        self.checkout() 
      
pizza_bot = PizzaBot()
pizza_bot.run()

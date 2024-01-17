#function to greet user
def welcome_message():
    print("Hello, welcome to Python-Counter!")
    print("What is your name?")
    name = input()
    print(f"Nice to meet you, {name}! My name is Harry.")
    return name

#fucntion to input user height
def get_height():
    print("What is your height in cm?")
    height = int(input())
    return height

#function to calculate ticker price
def calculate_ticket_price(age, height):
    a, b, c, d = 5, 7, 12, 3
    #checking height of user greater than 121
    if height >= 121:
        print(f"Your height is {height} cm, and you can ride today.")
        print("What is your age?")
        age = int(input())
        #checking ager of service user
        if age < 12:
            ticket_price = a
        elif age <= 18:
            ticket_price = b
        else:
            ticket_price = c
            
        #asking service user to charge for photograph 
        print(f"You are {age} years old, and your ticket will be £{ticket_price}.")
        print("Do you want a photo ticket? (Y/N)")
        photo = input().upper()
        if photo == "Y":
            ticket_price += d
            print(f"Your ticket plus photo will be £{ticket_price}")
        else:
            print(f"Have a nice day, and your grand total will be £{ticket_price}")
    else:
        print(f"Sorry, you are not tall enough to ride today. Your height is {height} cm.")
        
#defining main function to call all functions
def main():
    name = welcome_message()
    height = get_height()
    calculate_ticket_price(age=None, height=height)
    print("\nHopefully, you enjoyed it!")
    
main()

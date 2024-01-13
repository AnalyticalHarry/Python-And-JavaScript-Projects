#defining function for addition
def addition(num1, num2):
    sum_result = num1 + num2
    print(f"Addition of two numbers is {sum_result}")

#defining function for subtraction
def subtraction(num1, num2):
    sub_result = num1 - num2
    print(f"Subtraction of two numbers is {sub_result}")

#defining function for division
def division(num1, num2):
    #to avoid zero division error
    while True:
        if num2 == 0:
            print('Cannot divide by zero')
            print('Please enter a positive or negative number')
            return user()
        else:
            div_result = num1 / num2
            print(f'Division of two numbers is {div_result}')
            break

#defining function for multiplication
def multiplication(num1, num2):
    multi_result = num1 * num2
    print(f"Multiplication of two numbers is {multi_result}")

#defining function for user input and operations
def calculator(user_input, num1, num2):
    if user_input == "add":
        return addition(num1, num2)
    elif user_input == "sub":
        return subtraction(num1, num2)
    elif user_input == "div":
        return division(num1, num2)
    elif user_input == "multi":
        return multiplication(num1, num2)
    else:
        print("Please enter correct operations!!")

def user():
    user_input = input("Enter user operations: ")
    num1 = float(input("Enter number one: "))
    num2 = float(input("Enter number two: "))
    
    calculator(user_input, num1, num2)

user()

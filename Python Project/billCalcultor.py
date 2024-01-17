#function to calulate bills
def calculate_bill():
    print("Hello, what is your name?")
    print("")
    #user name input 
    name = input()
    print("")
    print("Nice to meet you,", name)
    print("Welcome to the Billing Service")
    #asking user to input total bill for split
    while True:
        ques_1 = input("\nHow much is the total bill? (£): ")
        try:
            ques_1 = float(ques_1)
            if ques_1 <= 0:
                raise ValueError("Total bill must be greater than zero.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive number for the total bill.")
    #asking user for total number of people to split bill
    while True:
        ques_2 = input("\nHow many people to split the bill with? ")
        try:
            ques_2 = int(ques_2)
            if ques_2 <= 0:
                raise ValueError("Number of people must be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the number of people.")
    #asking user, how much percentage of tips would each like to give
    while True:
        ques_3 = input("\nWhat percentage tip would you like to give? (e.g., 5, 10, 12, 15): ")
        try:
            ques_3 = int(ques_3)
            if ques_3 < 0:
                raise ValueError("Tip percentage cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer for the tip percentage.")
    #overall tips percentage calculated
    ans_3 = (ques_1 * ques_3 * 0.01)  
    print("\nOverall tips:", ans_3, "pounds")

    ans_2 = ans_3 / ques_2
    
    #individual tip distribution
    ans_1 = ques_1 / ques_2  
    #total sum of tip plus bill
    net_bill = ans_1 + ans_2  
    print("")
    print(f"Individual bill split {ques_3}% including tips is {net_bill:.2f} Pound")
  
calculate_bill()

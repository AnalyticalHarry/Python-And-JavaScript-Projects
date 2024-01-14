#importing libraries
import random

#function to roll dice
def roll_dice():
    print("Welcome to the Dice Rolling Simulator!")
    #while loop to run rolling dice features
    while True:
        #asking user to press enter button to roll dice
        input("Press Enter to roll the dice...")
        #using randint to randomly choosing number beteen 1, 6
        dice_roll = random.randint(1, 6)
        print(f'You rolled a {dice_roll}')
        #while to ask user to play again or close application
        while True:
            #taking input from user and converting them into lower case
            play_again = input("Would you like to roll again? (yes/no): ").lower()
            if play_again == "yes" or play_again == "no":
                break
            else:
                print("Please enter a valid option (yes/no)")
        if play_again == "no":
            print("Thanks for playing!")
            break
#calling roll_dice function
roll_dice()

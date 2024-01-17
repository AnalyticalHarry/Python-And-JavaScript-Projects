import datetime

def life_calculator():
    #welcome the user and ask for their name
    print("Hello, what is your name?")
    #read and store the user's name
    name = input()
    #friendly introduction
    print(f"Nice to meet you, {name}! You can call me Life Calculator.")
    #purpose of the following questions
    print(f"{name}, we are here to calculate your life expectancy, with a maximum value of 100 years.")
    print("")
    #the user's age
    print("Could you please share your age with us?")
    #user's age as an integer
    age = int(input())
    #birthdate by subtracting the user's age from the current year
    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    #maximum lifespan (100 years)
    max_lifespan = birth_year + 100
    #remaining years, months, and days based on the current date
    current_date = datetime.datetime.now()
    end_of_life_date = datetime.datetime(max_lifespan, current_date.month, current_date.day)
    #time difference between the current date and the end of life date
    time_remaining = end_of_life_date - current_date
    #remaining days, weeks, and months
    days_remaining = time_remaining.days
    weeks_remaining = days_remaining // 7
    months_remaining = days_remaining // 30
    #results in a user-friendly format
    print("")
    print(f"Based on your current age of {age} years, you have approximately:")
    print(f"- {days_remaining} days")
    print(f"- {weeks_remaining} weeks")
    print(f"- {months_remaining} months")
    print("left in your life, assuming a maximum lifespan of 100 years.")
    #friendly closing message
    print("Live life to the fullest and make the most of each day!")

life_calculator()

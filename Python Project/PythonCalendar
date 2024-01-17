#importing calendar 
import calendar

def generate_calendar():
    #welcome message
    print("Hello, welcome to Py Calendar!")
    #year the user wants to access
    print("Which year would you like to view (e.g., 2022)?")
    year = int(input())
    #width size of the calendar
    print("Enter the width size (1 to 6):")
    width = int(input())
    #TextCalendar object with the specified first weekday (0 for Monday)
    cal = calendar.TextCalendar(firstweekday=0)
    #calendar for the specified year with the given width
    calendar_data = cal.formatyear(year, width)
    print(f"\nYou have entered {year}, with a width size of {width}. Here is your calendar:\n")
    print(calendar_data)

generate_calendar()

def add_time(start_time, duration, starting_day=None):
    #parsing the start time
    start_time, meridiem = start_time.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_hour = start_hour % 12

    #parsing the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    #end time
    end_hour = start_hour + duration_hour
    end_minute = start_minute + duration_minute

    #carry-over of minutes
    if end_minute >= 60:
        end_hour += end_minute // 60
        end_minute %= 60

    #carry-over of hours
    carry_days = end_hour // 12
    end_hour %= 12

    #meridiem of the end time
    if carry_days % 2 != 0:
        if meridiem == 'AM':
            meridiem = 'PM'
        else:
            meridiem = 'AM'

    #0 hour to 12 hour
    if end_hour == 0:
        end_hour = 12

    #starting day of the week if provided
    if starting_day:
        starting_day = starting_day.lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        starting_day_index = days.index(starting_day)
        ending_day_index = (starting_day_index + carry_days) % 7
        ending_day = days[ending_day_index]

    #output string
    end_time = f"{end_hour:02d}:{end_minute:02d} {meridiem}"
    if starting_day:
        if carry_days == 1:
            end_time += f", {ending_day} (next day)"
        elif carry_days > 1:
            end_time += f", {ending_day} ({carry_days} days later)"
        else:
            end_time += f", {ending_day}"
    else:
        if carry_days == 1:
            end_time += " (next day)"
        elif carry_days > 1:
            end_time += f" ({carry_days} days later)"

    return end_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tuesday"))
print(add_time("6:30 PM", "205:12"))

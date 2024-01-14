import time

#function to timer
def Timer(hours=0, minutes=0, seconds=0):
    #total duration, which is in seconds
    duration = hours * 3600 + minutes * 60 + seconds
    #Current time
    start_time = time.time()
    #while loop to set timer, difference between curren time and time from user
    while time.time() - start_time < duration:
        #remaining time in seconds
        remaining_time = duration - (time.time() - start_time)
        #converting remaining time to hours, minutes, and seconds
        hours, remainder = divmod(int(remaining_time), 3600)
        minutes, seconds = divmod(remainder, 60)
        #remaining time in HH:MM:SS format on the same line
        print(f"Time remaining: {hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
        #pause for 1 second
        time.sleep(1)
        
    print("\nTime's Finished!")    

Timer(hours=0, minutes=0, seconds=10) 
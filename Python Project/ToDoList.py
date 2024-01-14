#function to add task
def add_task(do_list, task):
    #append python inbuilt function to add task
    do_list.append({"task": task, "completed": False})
    print(f"Task `{task}` added to do list.")

#fucntion to remove task
def remove_task(do_list, task):
    #for loop to iterate through "do_list" data
    for i in do_list:
        #comparing task from list and function parameter
        if i["task"] == task:
            #removing compared task from list
            do_list.remove(i)
            print(f"Task '{task}' removed from do list.")
            return
        print(f"Task '{task}' not found in do list.")
        
#function to define mark completed        
def mark_completed(do_list, task):
    #for loop to iterate inside "do_list" data
    for i in do_list:
        #comparing task from list and function parameter
        if i["task"] == task:
            #if if list task match with function parameter than mark it as completed
            i["completed"] = True
            print(f"Task '{task}' marked as completed.")
            return
    print(f"Task '{task}' not found in the to-do list.")
    
#fuction to show list    
def show_list(do_list):
    #print statement for empty list
    if not do_list:
        print("Do list is empty")
    else:
        print("Do list")
        #for loop to iterate inside do_list
        for i in do_list:
            #making status variable for print function, which can be used check task status
            status = "Completed" if i["completed"] else "Not Completed"
            print(f"- {i['task']} ({status})")
            
#declaring empty list, which is known as do list            
do_list = []

#adding task to "do_list" list 
add_task(do_list, "Buy groceries")
add_task(do_list, "Read a book")

#marking this task as completed
mark_completed(do_list, "Buy groceries")

#removing task from list
remove_task(do_list, "Read a book")

#showing "do_list" list
show_list(do_list)

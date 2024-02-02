#function for creating linear search
def linear_search(data, target):
    #for loop to iterate over length of array
    for i in range(len(data)):
        #comparing with help of index
        if data[i] == target:
            #return the index of the target element if found
            return i  
    #return -1 if the target element is not found
    return -1  

#list of element
my_list = [5, 2, 9, 1, 5, 6]
#selecting target elements
target_element = 9
#calling function
index = linear_search(my_list, target_element)

#control flow for printing result
if index != -1:
    print(f"Element {target_element} found at index {index}")
else:
    print(f"Element {target_element} not found in the list")

#function for binary_search function to search for a target element in a sorted array.
def binary_search(data, target):
    left, right = 0, len(data) - 1
    #while loop to perform binary search.
    while left <= right:
        #the middle index.
        mid = (left + right) // 2  
        if data[mid] == target:
            #return the index of the target element if found.
            return mid  
        elif data[mid] < target:
            #adjust the left boundary if the target is on the right.
            left = mid + 1  
        else:
            #adjust the right boundary if the target is on the left.
            right = mid - 1  
     #return -1 if the target element is not found.
    return -1 

#sorted list 
sorted_list = [1, 2, 5, 5, 6, 9]
#target
target_element = 6

#calling the binary_search function to find the index of the target element.
index = binary_search(sorted_list, target_element)

#control to print result
if index != -1:
    print(f"Element {target_element} found at index {index}")
else:
    print(f"Element {target_element} not found in the list")

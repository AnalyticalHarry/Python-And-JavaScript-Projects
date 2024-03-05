import math

def jump_search(arr, x):
    n = len(arr)
    # finding block size to be jumped
    step = math.sqrt(n)
    
    # finding the block where element is present 
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    
    # doing a linear search for x in the block beginning with prev
    while arr[int(prev)] < x:
        prev += 1
        
        # reached next block or end of array, element is not present
        if prev == min(step, n):
            return -1
    
    # element is found
    if arr[int(prev)] == x:
        return int(prev)
    
    return -1


data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
num = 17
print(f"Element {num} is at index " + str(jump_search(data, num)))

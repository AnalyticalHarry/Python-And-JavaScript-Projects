def counting_sort(arr):
    # find the maximum value in the array
    max_val = max(arr)  
     # count array to store count of each element
    count = [0] * (max_val + 1) 
     # an output array to store sorted elements
    output = [0] * len(arr) 

    # count the occurrences of each element
    for num in arr:
        count[num] += 1

    # modify count array to store the actual position of each element
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    # build the output array by placing elements in sorted order
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    # copy the output array to the original array
    for i in range(len(arr)):
        arr[i] = output[i]

data = [170, 45, 75, 90, 802, 24, 2, 66]
counting_sort(data)
print("Counting Sort:", data)

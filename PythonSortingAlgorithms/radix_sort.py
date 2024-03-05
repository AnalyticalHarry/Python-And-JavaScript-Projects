# function to perform counting sort with a given array and exponent
def counting_sort(arr, exp):
    # the length of the array
    n = len(arr)
    # an output array with zeros
    output = [0] * n
    # count array to store the count of occurrences of each digit
    count = [0] * 10

    # count the occurrences of each digit
    for i in range(n):
         # get the index of the current digit
        index = arr[i] // exp 
        # increment the count for the current digit
        count[index % 10] += 1  

    # cumulative sum of counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build the output array by placing elements in their sorted positions
    i = n - 1
    while i >= 0:
        # get the index of the current digit
        index = arr[i] // exp  
         # place the element in its sorted position
        output[count[index % 10] - 1] = arr[i] 
        # decrement the count for the current digit
        count[index % 10] -= 1  
        i -= 1

    # copy the sorted elements back to the original array
    for i in range(n):
        arr[i] = output[i]

# function to perform radix sort
def radix_sort(arr):
    # find the maximum value in the array
    max_val = max(arr)
    exp = 1
    # perform counting sort for each digit, starting from the least significant digit
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

data = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(data)
print("Radix Sort:", data)

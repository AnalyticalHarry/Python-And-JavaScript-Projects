def fibonacci_search(arr, x, n):
    # fibonacci numbers
    # (m-2)'th Fibonacci No.
    fibMMm2 = 0  
    # (m-1)'th Fibonacci No.
    fibMMm1 = 1  
    # m'th Fibonacci
    fibM = fibMMm2 + fibMMm1  

    # fibM is going to store the smallest Fibonacci
    # number greater than or equal to n
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # note that we compare arr[fibMMm2] with x.
    # when fibM becomes 1, fibMMm2 becomes 0
    while (fibM > 1):
        
        # fibMMm2 is a valid location
        i = min(offset + fibMMm2, n - 1)

        # If x is greater than the value at index fibMMm2,
        # cut the subarray array from offset to i
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # x is greater than the value at index fibMMm2,
        # cut the subarray after i+1
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # element found. return index
        else:
            return i

    # comparing the last element with x
    if(fibMMm1 and arr[offset + 1] == x):
        return offset + 1

    # element not found. return -1
    return -1


data = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
length_of_data = len(data)
num = 85
print("Found at index:", fibonacci_search(data, num, length_of_data))

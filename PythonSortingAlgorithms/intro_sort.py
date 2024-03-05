# importing libraries
import math

# insertion Sort for small subarrays
def insertionsort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        # move elements of A[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

# heap Sort for when the max depth is reached
def heapsort(A):
    def heapify(n, i):
        # Ilargest as root
        largest = i  
        # left = 2*i + 1
        l = 2 * i + 1  
        # right = 2*i + 2
        r = 2 * i + 2  

        # left child of root exists and is greater than root
        if l < n and A[l] > A[largest]:
            largest = l
        # right child of root exists and is greater than the largest so far
        if r < n and A[r] > A[largest]:
            largest = r
        # change root, if needed
        if largest != i:
            A[i], A[largest] = A[largest], A[i]  # swap
            # heapify the root.
            heapify(n, largest)

    n = len(A)
    # build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    # one by one extract elements
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(i, 0)

# partition the array into three parts: <pivot, ==pivot, >pivot
def partition(A):
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return left, middle, right

# intro sort logic
def introsort(A, maxdepth):
    n = len(A)
    # use insertion sort for small arrays
    if n < 16:
        insertionsort(A)
    # use heap sort when the recursion depth limit is reached
    elif maxdepth == 0:
        heapsort(A)
    else:
        # partition the array and sort the partitions recursively
        left, middle, right = partition(A)
        introsort(left, maxdepth - 1)
        introsort(right, maxdepth - 1)
        # combine the sorted partitions
        A[:] = left + middle + right

# entry point to start the sorting process
def sort(A):
    maxdepth = math.floor(math.log2(len(A))) * 2
    introsort(A, maxdepth)

data = [34, 7, 23, 32, 5, 62, 78, 4, 3, 31]
sort(data)
print(data)

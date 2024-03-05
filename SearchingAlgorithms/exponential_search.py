def binary_search(arr, lo, hi, x):
    if hi >= lo:
        mid = lo + (hi - lo) // 2
        # element is present at the middle itself
        if arr[mid] == x:
            return mid
        # element is smaller than mid, then it can only be present in left subarray
        if arr[mid] > x:
            return binary_search(arr, lo, mid - 1, x)
        # else the element can only be present in right subarray
        return binary_search(arr, mid + 1, hi, x)
    # element is not present in array
    return -1

def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    # finding the range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= x:
        i = i * 2
    # binary search for the found range
    return binary_search(arr, i // 2, min(i, len(arr)-1), x)


data = [2, 3, 4, 10, 40, 44, 55, 68, 77, 88, 99]
num = 10
result = exponential_search(data, num)
print(f"Element is present at index {result}")

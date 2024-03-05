def interpolation_search(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        # interpolation formula
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        # target found
        if arr[pos] == x:
            return pos
        # num is larger, num is in the upper part
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        # num is smaller, x is in the lower part
        if arr[pos] > x:
            return interpolation_search(arr, lo, pos - 1, x)
    
    return -1


data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
num = 18
index = interpolation_search(data, 0, len(data)-1, num)

print(f"Element found at index {index}")

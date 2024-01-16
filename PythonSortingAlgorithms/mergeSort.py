def merge_sort(data, ascending=True):
    #base case: return data if length is 1 or less
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    #recursively sort left and right halves
    left = merge_sort(left, ascending)
    right = merge_sort(right, ascending)

    #merge sorted halves
    return merge(left, right, ascending)

#merge function
def merge(left, right, ascending=True):
    result = []
    i = j = 0

    #merge left and right into result
    while i < len(left) and j < len(right):
        if ascending:
            #ascending order
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            #descending order
            if left[i] > right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    #extend result with remaining elements from left and right
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
#list of numbers from 1 to 20
data = [x for x in range(20, 0, -1)]
#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = merge_sort(data, ascending=True)
print("Sorted List Ascending:", sorted_data_ascending)

#descending sort
sorted_data_descending = merge_sort(data, ascending=False)
print("Sorted List Descending:", sorted_data_descending)

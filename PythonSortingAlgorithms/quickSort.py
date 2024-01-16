def quick_sort(data, ascending=True):
    #length of data
    length = len(data)
    #base case: return data if length is 1 or less
    if length <= 1:
        return data
    else:
        #choose pivot as the first element
        pivot = data[0]
        less_than_pivot = []
        greater_than_pivot = []

        #partition the data into two sublists based on pivot
        for i in data[1:]:
            if ascending:
                #append to less_than_pivot if sorting in ascending order
                if i <= pivot:
                    less_than_pivot.append(i)
                else:
                    greater_than_pivot.append(i)
            else:
                #append to less_than_pivot if sorting in descending order
                if i >= pivot:
                    less_than_pivot.append(i)
                else:
                    greater_than_pivot.append(i)

        #recursively sort sublists and combine with pivot
        return quick_sort(less_than_pivot, ascending) + [pivot] + quick_sort(greater_than_pivot, ascending)

#list of numbers from 1 to 20
data = [x for x in range(20, 0, -1)]
#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = quick_sort(data, ascending=True)
print("Sorted List Ascending:", sorted_data_ascending)

#descending sort
sorted_data_descending = quick_sort(data, ascending=False)
print("Sorted List Descending:", sorted_data_descending)

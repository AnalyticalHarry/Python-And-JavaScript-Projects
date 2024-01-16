def quick_sort(data, ascending=True):
    length = len(data)
    if length <= 1:
        return data
    else:
        pivot = data[0]
        less_than_pivot = []
        greater_than_pivot = []
        
        for i in data[1:]:
            if ascending:
                if i <= pivot:
                    less_than_pivot.append(i)
                else:
                    greater_than_pivot.append(i)
                
            else:
                if i >= pivot:
                    less_than_pivot.append(i)
                else:
                    greater_than_pivot.append(i)
                    
        return quick_sort(less_than_pivot, ascending) + [pivot] + quick_sort(greater_than_pivot, ascending)
    
#list of numbers from 1 to 20 
data = [x for x in range(1, 21)]
#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = quick_sort(data, ascending=True)
print("Sorted List Ascending", sorted_data_ascending)
#descending sort
sorted_data_descending = quick_sort(data, ascending=False)
print("Sorted List Descending", sorted_data_descending)
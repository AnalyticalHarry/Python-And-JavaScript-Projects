def selection_sort(data, ascending=True):
    #length of the data
    length = len(data)
    
    #for loop to iterate through the list
    for i in range(length):
        min_index = i
        
        #find the minimum element in the unsorted part of the list
        for j in range(i + 1, length):
            if ascending:
                #ascending order
                if data[j] < data[min_index]:
                    min_index = j
            else:
                #descending order
                if data[j] > data[min_index]:
                    min_index = j

        #swap the found minimum element with the current element
        data[i], data[min_index] = data[min_index], data[i]

    return data

    
#list of numbers from 1 to 20
data = [x for x in range(20, 0, -1)]
#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = selection_sort(data, ascending=True)
print("Sorted List Ascending:", sorted_data_ascending)

#descending sort
sorted_data_descending = selection_sort(data, ascending=False)
print("Sorted List Descending:", sorted_data_descending)

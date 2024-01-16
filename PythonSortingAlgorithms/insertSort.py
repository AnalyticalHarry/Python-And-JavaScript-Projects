def insert_sort(data, ascending=True):
    #length of the data
    length = len(data)
    
    #for loop to iterate over the elements starting from the second one
    for i in range(1, length):
        # Store the current element in a variable
        key = data[i]
        
        #initialise the index for comparison to the left of the current element
        j = i - 1
        
        #if sorting in ascending order
        if ascending:
            #moving elements greater than key to the right
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j = j - 1
            
        #if sorting in descending order
        else:
            #moving elements smaller than key to the right
            while j >= 0 and key > data[j]:
                data[j + 1] = data[j]
                j = j - 1
                
        #insert the key at its correct position
        data[j + 1] = key
        
    #return the sorted data
    return data 

#list of numbers from 1 to 20 
data = [x for x in range(20, 0, -1)]

#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = insert_sort(data, ascending=True)
print("Sorted List Ascending:", sorted_data_ascending)

#descending sort
sorted_data_descending = insert_sort(data, ascending=False)
print("Sorted List Descending:", sorted_data_descending) 
            

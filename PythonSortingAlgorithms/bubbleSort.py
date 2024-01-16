def bubble_sort(data, ascending=True):
    #length of data
    length = len(data)
      #for lopp to iterate through the list (outer loop)
    for i in range(length - 1):
        #for loop iterate through the unsorted part of the list (inner loop)
        for j in range(0, length - i - 1):
            if ascending:
                #if sorting is in ascending order
                if data[j] > data[j + 1]:
                     #swap the current element, if greater than the next element
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                #if sorting in descending order
                if data[j] < data[j+1]:
                    #swap the current elements is less than the next
                    data[j], data[j + 1] = data[j+1], data[j]

#list of numbers from 1 to 20 
data = [x for x in range(1, 21)]
#original list
print("Original List:", data)

#ascending sort
sorted_data_ascending = bubble_sort(data, ascending=True)
print("Sorted List Ascending", sorted_data_ascending)
#descending sort
sorted_data_descending = bubble_sort(data, ascending=False)
print("Sorted List Descending", sorted_data_descending)

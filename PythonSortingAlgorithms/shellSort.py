def shell_sort(data, ascending=True):
    #length of the data
    n = len(data)
    
    #initial gap to half of the list size
    gap = n // 2

    #while loop to iterate over the list with decreasing gap sizes
    while gap > 0:
        #for loop to iterate over elements starting from the gap
        for i in range(gap, n):
            temp = data[i]
            j = i

            #compare and swap elements with a gap
            while j >= gap and (data[j - gap] > temp if ascending else data[j - gap] < temp):
                data[j] = data[j - gap]
                j -= gap

            #place the current element at its correct position
            data[j] = temp

        #reduce the gap for the next iteration
        gap //= 2



#list of numbers from 20 to 1
data = [x for x in range(20, 0, -1)]

#the original list
print("Original List:", data)

#ascending Shell Sort
shell_sort(data, ascending=True)
print("Sorted List Ascending:", data)

#descending Shell Sort
shell_sort(data, ascending=False)
print("Sorted List Descending:", data)

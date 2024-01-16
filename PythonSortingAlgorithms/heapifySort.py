#function to compare two values 
def compare(x, y, ascending=True):
    if ascending:
        return x > y
    else:
        return x < y

#function to heapify a subtree rooted at index i 
def heapify(data, n, i, ascending=True):
    #initilise the largest as the root
    largest = i
    #indices of the left and right children of the current node
    left = 2 * i + 1
    right = 2 * i + 2

    #compare the left child with the largest node, update if necessary
    if left < n and compare(data[left], data[largest], ascending):
        largest = left

    #compare the right child with the largest node, update if necessary
    if right < n and compare(data[right], data[largest], ascending):
        largest = right

    #if the largest node is not the root, swap and recursively heapify the affected subtree
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest, ascending)

#defining heap_sort function
def heap_sort(data, ascending=True):
    #length of the data array
    n = len(data)

    #max-heap by heapifying non-leaf nodes
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, ascending)

    #elements from the heap one by one and swap with the root
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        # Heapify the reduced heap
        heapify(data, i, 0, ascending)


#list of numbers from 1 to 20
data = [x for x in range(20, 0, -1)]
#original list
print("Original List:", data)

#ascending order
ascending_order = True  
heap_sort(data, ascending=ascending_order)

#sorted list 
print(f"Sorted List using Heap Sort ({'Ascending' if ascending_order else 'Descending'}):", data)

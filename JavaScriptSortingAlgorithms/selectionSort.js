function selectionSort(data, ascending = true) {
    //the length of the input array 'data'
    const length = data.length;

    //for loop to iterate over the elements of the array
    for (let i = 0; i < length; i++) {
        //initialise a variable minIndex to the current index i
        let minIndex = i;

        //nested loop to find the index of the minimum/maximum element
        for (let j = i + 1; j < length; j++) {
            // Check if sorting is in ascending order
            if (ascending) {
                //data[j] is smaller than data[minIndex], update minIndex to j
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            } else {
                //if sorting is in descending order, update minIndex if data[j] is larger
                if (data[j] > data[minIndex]) {
                    minIndex = j;
                }
            }
        }

        //swap the element at i with the element at minIndex
        [data[i], data[minIndex]] = [data[minIndex], data[i]];
    }

    //return the sorted array
    return data;
}

//numbers from 1 to 20 in descending order 
const data = Array.from({ length: 20 }, (_, i) => 20 - i)
console.log("Original List:", data);

//ascending order 
const sortedDataAscending = selectionSort([...data], true);
console.log("Sorted List Ascending:", sortedDataAscending);

//descending order 
const sortedDataDescending = selectionSort([...data], false);
console.log("Sorted List Descending:", sortedDataDescending);

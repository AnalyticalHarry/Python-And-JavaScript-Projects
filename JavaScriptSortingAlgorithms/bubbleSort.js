function bubbleSort(data, ascending = true) {
    //length of data
    var length = data.length;

    //outer loop to iterate through the list
    for (var i = 0; i < length - 1; i++) {
        //inner loop iterates through the unsorted part of the list
        for (var j = 0; j < length - i - 1; j++) {
            //swap if sorting in ascending order and the current element is greater than the next element
            //or swap if sorting in descending order and the current element is less than the next element
            if ((ascending && data[j] > data[j + 1]) || (!ascending && data[j] < data[j + 1])) {
                //swap the current element with the next element
                [data[j], data[j + 1]] = [data[j + 1], data[j]];
            }
        }
    }

    return data;
}

//list of numbers from 1 to 20
var data = Array.from({ length: 20 }, (i, index) => 20 - index);

//original list
console.log("Original List:", data);

//ascending sort
var sortedDataAscending = bubbleSort(data, true);
console.log("Sorted List Ascending:", sortedDataAscending);

//descending sort
var sortedDataDescending = bubbleSort(data, false);
console.log("Sorted List Descending:", sortedDataDescending);
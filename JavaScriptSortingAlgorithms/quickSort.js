function quickSort(data, ascending = true) {
  //length of data
  const length = data.length;

  //return data if length is 1 or less
  if (length <= 1) {
    return data;
  } else {
    //choose pivot as the first element
    const pivot = data[0];
    const lessThanPivot = [];
    const greaterThanPivot = [];

    //partition the data into two sublists based on pivot
    for (let i = 1; i < length; i++) {
      if (ascending) {
        //append to lessThanPivot if sorting in ascending order
        if (data[i] <= pivot) {
          lessThanPivot.push(data[i]);
        } else {
          greaterThanPivot.push(data[i]);
        }
      } else {
        //append to lessThanPivot if sorting in descending order
        if (data[i] >= pivot) {
          lessThanPivot.push(data[i]);
        } else {
          greaterThanPivot.push(data[i]);
        }
      }
    }

    //recursively sort sublists and combine with pivot
    return [...quickSort(lessThanPivot, ascending), pivot, ...quickSort(greaterThanPivot, ascending)];
  }
}

//list of numbers from 1 to 20 in reverse order
const data = Array.from({ length: 20 }, (_, i) => 20 - i);
console.log("Original List:", data);

//ascending sort
const sortedDataAscending = quickSort(data, true);
console.log("Sorted List Ascending:", sortedDataAscending);
//descending sort
const sortedDataDescending = quickSort(data, false);
console.log("Sorted List Descending:", sortedDataDescending);

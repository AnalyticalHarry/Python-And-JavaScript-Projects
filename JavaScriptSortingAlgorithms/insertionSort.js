function insertionSort(data, ascending = true) {
  //length of the data array
  const length = data.length;

  //iterate over the elements starting from the second one
  for (let i = 1; i < length; i++) {
    //store the current element in a variable called key
    const key = data[i];

    //initialise an index for comparison to the left of the current element
    let j = i - 1;

    //sorting in ascending order
    if (ascending) {
      //elements greater than key to the right
      while (j >= 0 && key < data[j]) {
        //shift the greater element to the right
        data[j + 1] = data[j]; 
        //decrement the index to compare with the next element
        j--; 
      }
    } else {
      //move elements smaller than key to the right (for descending order)
      while (j >= 0 && key > data[j]) {
        //shift the smaller element to the right
        data[j + 1] = data[j]; 
        //decrement the index to compare with the next element
        j--; 
      }
    }

    //insert the key at its correct position
    data[j + 1] = key;
  }

  //return the sorted data array
  return data;
}

//numbers from 20 to 1 in reverse order
const data = Array.from({ length: 20 }, (_, i) => 20 - i);
console.log("Original List:", data);

//ascending Insertion Sort
insertionSort(data, true);
console.log("Sorted List Ascending:", data);
//descending Insertion Sort
insertionSort(data, false);
console.log("Sorted List Descending:", data);

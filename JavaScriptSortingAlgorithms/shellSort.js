function shellSort(data, ascending = true) {
    // length of dataset
    const n = data.length;
  //splitting length of data into twp part
    let gap = Math.floor(n / 2);
  //while loop to iterate over the list with decreasing gap sizes
    while (gap > 0) {
      //for loop to iterate over elements starting from the gap
      for (let i = gap; i < n; i++) {
        const temp = data[i];
        let j = i;
        //compare and swap elements with a gap
        while (j >= gap && (ascending ? data[j - gap] > temp : data[j - gap] < temp)) {
          data[j] = data[j - gap];
          j -= gap;
        }
        //place the current element at its correct position
        data[j] = temp;
      }
      //reduce the gap for the next iteration
      gap = Math.floor(gap / 2);
    }
  }
  
  //numbers from 20 to 1 in reverse order
  const data = Array.from({ length: 20 }, (_, i) => 20 - i);
  console.log("Original List:", data);
  
  //ascending Shell Sort
  shellSort(data, true);
  console.log("Sorted List Ascending:", data);
  
  //descending Shell Sort
  shellSort(data, false);
  console.log("Sorted List Descending:", data);
  

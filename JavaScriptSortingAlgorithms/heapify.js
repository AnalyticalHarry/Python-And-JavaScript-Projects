// function to compare two values
function compare(x, y, ascending = true) {
  if (ascending) {
    return x > y;
  } else {
    return x < y;
  }
}

// function to heapify a subtree rooted at index i
function heapify(data, n, i, ascending = true) {
  // initialise the largest as the root
  let largest = i;
  // Indices of the left and right children of the current node
  const left = 2 * i + 1;
  const right = 2 * i + 2;

  // compare the left child with the largest node, update if necessary
  if (left < n && compare(data[left], data[largest], ascending)) {
    largest = left;
  }

  // compare the right child with the largest node, update if necessary
  if (right < n && compare(data[right], data[largest], ascending)) {
    largest = right;
  }

  // if the largest node is not the root, swap and recursively heapify the affected subtree
  if (largest !== i) {
    const temp = data[i];
    data[i] = data[largest];
    data[largest] = temp;
    heapify(data, n, largest, ascending);
  }
}

// defining heapSort function
function heapSort(data, ascending = true) {
  // Length of the data array
  const n = data.length;

  // build max-heap by heapifying non-leaf nodes
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapify(data, n, i, ascending);
  }

  // extract elements from the heap one by one and swap with the root
  for (let i = n - 1; i > 0; i--) {
    const temp = data[0];
    data[0] = data[i];
    data[i] = temp;
    // Heapify the reduced heap
    heapify(data, i, 0, ascending);
  }
}

// list of numbers from 1 to 20
const data = [...Array(20).keys()].map(x => x + 1).reverse();
console.log("Original List:", data);

// ascending order
const ascendingOrder = true;
heapSort(data, ascendingOrder);

// sorted list
console.log(`Sorted List using Heap Sort (${ascendingOrder ? 'Ascending' : 'Descending'}):`, data);

function countingSort(arr) {
    // find the maximum value in the array
    let maxVal = Math.max(...arr);
    // count array to store count of each element
    let count = new Array(maxVal + 1).fill(0);
    // an output array to store sorted elements
    let output = new Array(arr.length).fill(0);

    // count the occurrences of each element
    arr.forEach(num => {
        count[num]++;
    });

    // modify count array to store the actual position of each element
    for (let i = 1; i <= maxVal; i++) {
        count[i] += count[i - 1];
    }

    // build the output array by placing elements in sorted order
    for (let i = arr.length - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // copy the output array to the original array
    for (let i = 0; i < arr.length; i++) {
        arr[i] = output[i];
    }
}

let data = [170, 45, 75, 90, 802, 24, 2, 66];
countingSort(data);
console.log("Counting Sort:", data);

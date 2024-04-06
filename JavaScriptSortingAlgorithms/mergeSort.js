function mergeSort(data, ascending = true) {
    if (data.length <= 1) {
        return data;
    }

    const mid = Math.floor(data.length / 2);
    const left = data.slice(0, mid);
    const right = data.slice(mid);

    return merge(mergeSort(left, ascending), mergeSort(right, ascending), ascending);
}

function merge(left, right, ascending = true) {
    let result = [];
    let i = 0;
    let j = 0;

    while (i < left.length && j < right.length) {
        if (ascending) {
            if (left[i] < right[j]) {
                result.push(left[i]);
                i++;
            } else {
                result.push(right[j]);
                j++;
            }
        } else {
            if (left[i] > right[j]) {
                result.push(left[i]);
                i++;
            } else {
                result.push(right[j]);
                j++;
            }
        }
    }

    return result.concat(left.slice(i)).concat(right.slice(j));
}

const data = Array.from({ length: 20 }, (_, i) => 20 - i);
console.log("Original List:", data);

const sortedDataAscending = mergeSort(data, true);
console.log("Sorted List Ascending:", sortedDataAscending);

const sortedDataDescending = mergeSort(data, false);
console.log("Sorted List Descending:", sortedDataDescending);

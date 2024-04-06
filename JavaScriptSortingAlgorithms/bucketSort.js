function insertSort(data, ascending = true) {
    const length = data.length;

    for (let i = 1; i < length; i++) {
        const key = data[i];
        let j = i - 1;

        if (ascending) {
            while (j >= 0 && key < data[j]) {
                data[j + 1] = data[j];
                j = j - 1;
            }
        } else {
            while (j >= 0 && key > data[j]) {
                data[j + 1] = data[j];
                j = j - 1;
            }
        }

        data[j + 1] = key;
    }

    return data;
}

function bucketSort(data, ascending = true) {
    const buckets = Array.from({ length: 10 }, () => []);

    for (let num of data) {
        const index = Math.floor(num / 10);
        buckets[index].push(num);
    }

    let result = [];

    for (let bucket of buckets) {
        insertSort(bucket, ascending);

        if (ascending) {
            result = result.concat(bucket);
        } else {
            result = bucket.concat(result);
        }
    }

    return result;
}

// array of numbers from 20 to 1
const data = Array.from({ length: 20 }, (_, i) => 20 - i);
console.log("Original List:", data);

// sort in ascending order
const sortedDataAscending = bucketSort(data, true);
console.log("Sorted List Ascending:", sortedDataAscending);

// sort in descending order
const sortedDataDescending = bucketSort(data, false);
console.log("Sorted List Descending:", sortedDataDescending);

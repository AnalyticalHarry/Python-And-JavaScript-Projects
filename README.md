- Bubble Sort - While not efficient for large datasets, it's often introduced for educational purposes.
- Selection Sort - Similarly, it's simple but not suitable for large datasets.
- Insertion Sort - Effective for small datasets or nearly sorted arrays.
- Merge Sort - Highly efficient and stable, suitable for large datasets.
- Quick Sort - Known for its performance and commonly used in practical applications.
- Heap Sort - Efficient for large datasets, offering O(n log n) complexity.
- Radix Sort - Non-comparative, good for fixed-length integer sorting.
- Bucket Sort - Useful in specific scenarios where the data is uniformly distributed.
- Counting Sort - Efficient for sorting small integers or non-comparative sorting scenarios.
- Shell Sort - An improvement on insertion sort, better for medium-sized arrays.
- Timsort - A hybrid sorting algorithm derived from merge sort and insertion sort, used in Python’s sorted() and Java’s Arrays.sort().
- IntroSort - A hybrid sort used in the C++ Standard Library's sort function, combining quicksort, heapsort, and insertion sort.

## Linear Search

- **Description**: Iterates through a list sequentially to find a target value. Simple and straightforward but inefficient for large datasets.

## Binary Search

- **Description**: Efficiently finds a target value within a sorted array by repeatedly dividing the search interval in half. Requires a sorted dataset.

## Jump Search

- **Description**: A block search algorithm that works on sorted arrays. It creates a block and tries to find the element in that block, then performs a linear search within the block to find the target element. More efficient than Linear Search for sorted arrays.

## Interpolation Search

- **Description**: Similar to binary search but calculates the probable position of the target value based on the lowest and highest values in the dataset. Can be more efficient than binary search for certain data distributions.

## Exponential Search

- **Description**: Involves determining a range where the element might be present by repeatedly doubling it, then using binary search within that range. Useful for unbounded or infinite arrays.

## Fibonacci Search

- **Description**: Works on sorted arrays using Fibonacci numbers to divide the array and reduce the search space. Similar to binary search but uses a Fibonacci sequence to determine the split point.

## Depth-First Search (DFS)

- **Description**: An algorithm for traversing or searching tree or graph data structures. It starts at the root and explores as far as possible along each branch before backtracking.

## Breadth-First Search (BFS)

- **Description**: Explores tree or graph data structures by starting at the root and exploring all neighbor nodes at the current depth before moving on to nodes at the next depth level.

## Uniform Cost Search (UCS)

- **Description**: Used for traversing a weighted tree or graph. It finds the least cost path from the start node to the goal node.

## A* Search Algorithm

- **Description**: Widely used in pathfinding and graph traversal, efficiently finding the shortest path between nodes in a graph, such as road networks.

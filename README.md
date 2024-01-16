# Sorting Algorithms

Sorting algorithms arrange elements in a specific order. Here are explanations for various sorting algorithms:

## 1. Bubble Sort

- **Algorithm:**
  - Simple sorting algorithm.
  - Compares adjacent elements and swaps them if they are in the wrong order.
  - Repeats the process until the list is sorted.

## 2. Selection Sort

- **Algorithm:**
  - Divides the array into sorted and unsorted regions.
  - Repeatedly selects the minimum element from the unsorted region and swaps it with the first element.
  
## 3. Insertion Sort

- **Algorithm:**
  - Builds the sorted array one element at a time.
  - Takes each element and inserts it into its correct position in the already sorted part of the array.

## 4. Merge Sort

- **Algorithm:**
  - Divide-and-conquer algorithm.
  - Divides the array into two halves, recursively sorts them, and then merges them.
  - Guarantees a time complexity of O(n log n).

## 5. Quick Sort

- **Algorithm:**
  - Divide-and-conquer algorithm.
  - Chooses a "pivot" element and partitions the array into two sub-arrays.
  - Recursively sorts the sub-arrays.
  - Efficient for large datasets.

## 6. Heap Sort

- **Algorithm:**
  - Uses a binary heap data structure.
  - Builds a max heap and repeatedly extracts the maximum element.
  - In-place sorting algorithm with a time complexity of O(n log n).

## 7. Radix Sort

- **Algorithm:**
  - Sorting by distributing elements into buckets according to their individual digits.
  - Can be used for integers or strings.
  - Linear time complexity for certain scenarios.

## 8. Bucket Sort

- **Algorithm:**
  - Distributes elements into a number of buckets and then sorts each bucket.
  - Requires knowledge of the input range.

## 9. Counting Sort

- **Algorithm:**
  - Assumes that the input elements are integers within a known range.
  - Counts the occurrence of each element and computes the final position.

## 10. Shell Sort

- **Algorithm:**
  - Variation of insertion sort.
  - Compares elements that are far apart and progressively reduces the gap.

## 11. Cocktail Shaker Sort

- **Algorithm:**
  - Variation of the bubble sort.
  - Iteratively moves through the list in both directions, repeatedly swapping adjacent elements.

## 12. Gnome Sort

- **Algorithm:**
  - Simple sorting algorithm.
  - Similar to insertion sort but moves elements to their proper place by a series of swaps.

## 13. Odd-Even Sort

- **Algorithm:**
  - Parallel sorting algorithm suitable for parallel processors.
  - Compares and swaps elements in pairs, first checking and swapping odd-indexed pairs and then even-indexed pairs.

## 14. Pancake Sorting

- **Algorithm:**
  - Sorting by prefix reversal.
  - Repeatedly reverses portions of the array to sort it.

## 15. Stooge Sort

- **Algorithm:**
  - Recursive sorting algorithm.
  - Divides the array into three parts and recursively sorts the first two-thirds and the last two-thirds.

## 16. Bogo Sort

- **Algorithm:**
  - Not a practical sorting algorithm.
  - Randomly permutes the elements until the list is sorted.

## 17. Bozo Sort

- **Algorithm:**
  - Another impractical sorting algorithm.
  - Randomly swaps elements until the list is sorted.

## 18. Comb Sort

- **Algorithm:**
  - Improves upon bubble sort.
  - Eliminates small values near the end of the list quickly.

## 19. Pigeonhole Sort

- **Algorithm:**
  - Suitable for lists where the number of elements and the range of possible key values are approximately the same.

## 20. Bead Sort (Gravity Sort)

- **Algorithm:**
  - Conceptual sorting algorithm using gravity.
  - Beads slide down the rows and collect at the bottom, forming a sorted sequence.
 
## 21. Sleep Sort

- **Algorithm:**
  - Unconventional sorting algorithm.
  - Each element is pushed onto a separate thread with a sleep time proportional to its value.

## 22. Quantum Bogosort

- **Algorithm:**
  - A playful, fictional algorithm.
  - The state of the entire universe is considered to perform sorting.

## 23. Patience Sort

- **Algorithm:**
  - Used for playing the card game "patience."
  - Simulates how cards are sorted into piles based on values.

## 24. Postman Sort

- **Algorithm:**
  - Sorting technique inspired by postal workers.
  - Focuses on minimizing the total distance traveled.

## 25. Brick Sort

- **Algorithm:**
  - A variation of insertion sort.
  - Moves elements to their final position by a series of adjacent swaps.

## 26. Comb Gnome Sort

- **Algorithm:**
  - A combination of comb sort and gnome sort.
  - Uses a series of gap values for comparing and swapping elements.

## 27. Timsort

- **Algorithm:**
  - Hybrid sorting algorithm derived from merge sort and insertion sort.
  - Used as the default sorting algorithm in Python's `sorted()` function.

## 28. Library Sort

- **Algorithm:**
  - Sorting technique that relies on a subroutine to decide the correct order of elements.
  - Library sort uses a binary search algorithm for this purpose.

## 29. Shellsort (Shell Sort)

- **Algorithm:**
  - Improves upon insertion sort by allowing the comparison and exchange of elements that are far apart.
  - Uses a sequence of diminishing gaps for sorting.

## 30. Bitonic Sort

- **Algorithm:**
  - Efficient parallel sorting algorithm.
  - Requires the input size to be a power of two.

## 31. Cycle Sort

- **Algorithm:**
  - In-place sorting algorithm.
  - Reduces the number of memory writes to a minimum.

## 32. Flash Sort

- **Algorithm:**
  - Distribution sorting algorithm.
  - Efficient for datasets with a large number of duplicated elements.

## 33. Smoothsort

- **Algorithm:**
  - Hybrid sorting algorithm.
  - Combines the principles of heapsort and smoothsort.

## 34. Spreadsort

- **Algorithm:**
  - Sorting algorithm designed for parallel computing.
  - Efficient for large datasets.

## 35. Unshuffle Sort

- **Algorithm:**
  - Unusual sorting technique.
  - Randomly permutes the input until it is sorted.

## 36. Spaghetti Sort

- **Algorithm:**
  - Humorous and impractical sorting algorithm.
  - Involves sorting a list of elements by cooking them as spaghetti.

## 37. Dutch National Flag Algorithm

- **Algorithm:**
  - Sorting algorithm designed to sort an array of elements that belong to three distinct groups.
  - Efficient for sorting arrays with multiple values.

## 38. Smooth Sort

- **Algorithm:**
  - Combines the principles of heapsort and insertion sort.
  - Optimized for partially ordered data.

## 39. IntroSort

- **Algorithm:**
  - Hybrid sorting algorithm.
  - Uses quicksort, heapsort, and insertion sort in combination.

## 40. Gapped Insertion Sort

- **Algorithm:**
  - A variation of insertion sort.
  - Allows elements to move in larger steps toward their final position.

## 41. Cube Sort

- **Algorithm:**
  - Sorting algorithm inspired by the Rubik's Cube.
  - Divides the data into sub-cubes and performs sorting operations.

## 42. Odd-Even Merge Sort

- **Algorithm:**
  - Parallel sorting algorithm.
  - Combines the principles of odd-even sort and merge sort.

## 43. Tournament Sort

- **Algorithm:**
  - Sorting algorithm based on tournament-style comparisons.
  - Often used in parallel processing.

## 44. Sleepy Sort

- **Algorithm:**
  - Humorous sorting algorithm.
  - Elements are compared only when they are awake.

## 45. Pancake Sorting (Variation)

- **Algorithm:**
  - Variation of pancake sorting.
  - Involves reversing segments of the array to sort it.

## 46. Bidirectional Bubble Sort

- **Algorithm:**
  - Variation of bubble sort.
  - Compares and swaps elements bidirectionally.

## 47. Comb Odd-Even Sort

- **Algorithm:**
  - Merges the principles of comb sort and odd-even sort.
  - Uses both odd and even passes for sorting.

## 48. Time Sort

- **Algorithm:**
  - Sorting algorithm inspired by time-based principles.
  - Elements are assigned timestamps and sorted accordingly.

## 49. Organ Pipe Sort

- **Algorithm:**
  - Sorting algorithm inspired by the physics of organ pipes.
  - Uses oscillation patterns for sorting.

## 50. Fibonacci Heap Sort

- **Algorithm:**
  - Sorting algorithm based on Fibonacci heaps.
  - Primarily used for priority queue operations.

## 51. Billiard Sort

- **Algorithm:**
  - Sorting algorithm inspired by the motion of billiard balls.
  - Elements are compared and moved like balls colliding on a billiard table.

## 52. Grail Sort

- **Algorithm:**
  - Hybrid sorting algorithm.
  - Utilizes an external memory in the sorting process.

## 53. Library Merge Sort

- **Algorithm:**
  - Variation of merge sort.
  - Incorporates the concept of library sorting.

## 54. Odd-Even QuickSort

- **Algorithm:**
  - A variation of quicksort.
  - Uses odd-even transposition for sorting.

## 55. Batcher's Odd-Even Mergesort

- **Algorithm:**
  - Parallel sorting algorithm.
  - Merges the principles of odd-even mergesort and Batcher's bitonic sort.

## 56. Bidirectional Merge Sort

- **Algorithm:**
  - Variation of merge sort.
  - Elements are merged bidirectionally.

## 57. FlashSort

- **Algorithm:**
  - Sorting algorithm designed for datasets with a large number of duplicated elements.
  - Efficient for certain scenarios.

## 58. Smoothsort (Sedgewick)

- **Algorithm:**
  - Variation of smoothsort introduced by Robert Sedgewick.
  - Combines the principles of heapsort and insertion sort.

## 59. Stupid Sort

- **Algorithm:**
  - Humorous and impractical sorting algorithm.
  - Repeatedly shuffles the list until it is sorted.

## 60. Strand Sort

- **Algorithm:**
  - Sorting algorithm that repeatedly takes elements from the unsorted list and builds a sorted one.

## 61. Turbo Sort

- **Algorithm:**
  - Variation of quicksort.
  - Optimized for practical performance.

## 62. Spin Sort

- **Algorithm:**
  - Sorting algorithm inspired by the motion of a spinning object.
  - Elements are moved in a circular pattern.

## 63. Introselect

- **Algorithm:**
  - Hybrid sorting algorithm.
  - Combines quicksort, heapsort, and insertion sort.

## 64. Unbalanced Bubble Sort

- **Algorithm:**
  - Variation of bubble sort.
  - Randomly swaps elements with a probability based on their values.

## 65. Gravitational Sort

- **Algorithm:**
  - Sorting inspired by the force of gravity.
  - Elements are moved downward to their sorted positions.

## 66. Merge Exchange Sort

- **Algorithm:**
  - Combines principles of merge sort and exchange sort.
  - Elements are merged and exchanged for sorting.

## 67. Shear Sort

- **Algorithm:**
  - Parallel sorting algorithm inspired by shearing operations.
  - Suitable for sorting matrices.

## 68. Bidirectional Selection Sort

- **Algorithm:**
  - Variation of selection sort.
  - Selects both the minimum and maximum elements in each pass.

## 69. Smoothsort (Heapless)

- **Algorithm:**
  - Variation of smoothsort without using a heap.
  - Optimized for memory usage.

## 70. Reverse Sorting

- **Algorithm:**
  - Unconventional sorting approach.
  - Sorts the array in descending order.
 

## 70. Reverse Sorting

- **Algorithm:**
  - Unconventional sorting approach.
  - Sorts the array in descending order.

## 71. Population Count Sort

- **Algorithm:**
  - Sorting algorithm based on counting the number of set bits in binary representations.
  - Efficient for sorting integers.

## 72. Self-Organizing List

- **Algorithm:**
  - Adaptive sorting strategy.
  - Adjusts the order of elements based on their frequency of access.

## 73. Super Smoothsort

- **Algorithm:**
  - Enhanced version of smoothsort.
  - Further optimizations for better performance.

## 74. Tangle Sort

- **Algorithm:**
  - Sorting inspired by the movement of tangled strings.
  - Elements are rearranged to untangle the structure.

## 75. Batcher's Bitonic Mergesort

- **Algorithm:**
  - Parallel sorting algorithm.
  - Incorporates the principles of bitonic sort and mergesort.

## 76. FlashSort (Bucketless)

- **Algorithm:**
  - Variation of flashsort without using buckets.
  - Adapts the distribution sorting approach.

## 77. Introspective Priority Queue Sort

- **Algorithm:**
  - Sorting algorithm based on priority queues.
  - Combines introsort with priority queue operations.

## 78. External Sorting

- **Algorithm:**
  - Techniques for sorting data that doesn't fit entirely into memory.
  - Involves efficient disk-based sorting strategies.

## 79. Deap Sort

- **Algorithm:**
  - Hybrid sorting algorithm combining principles of heapsort and double-ended priority queues.
  - Aims for better performance on partially ordered data.

## 80. Quickersort

- **Algorithm:**
  - Variation of quicksort with additional optimizations.
  - Focuses on minimizing comparisons and swaps.

## 81. Optimistic Sorting

- **Algorithm:**
  - Sorting algorithm with optimistic assumptions about the order of elements.
  - Adjusts its strategy based on the initial state of the data.

## 82. Adaptive Merge Sort

- **Algorithm:**
  - Variation of merge sort with adaptability to the data.
  - Adjusts its behavior based on the properties of the input.

## 83. Bidirectional Merge Exchange Sort

- **Algorithm:**
  - Merges principles of bidirectional merge sort and exchange sort.
  - Elements are merged bidirectionally and exchanged for sorting.

## 84. Shellsort (Tokuda Gap Sequence)

- **Algorithm:**
  - Variation of Shellsort using the gap sequence proposed by Tokuda.
  - Optimized for practical performance.

## 85. In-Place Radix Sort

- **Algorithm:**
  - Variation of radix sort optimized for in-place sorting.
  - Sorts elements based on individual digits.

## 86. Tree Sort

- **Algorithm:**
  - Sorting algorithm that builds a binary search tree.
  - In-order traversal retrieves sorted elements.

## 87. Binary Merge Sort

- **Algorithm:**
  - Variation of merge sort using binary partitioning.
  - Efficient for large datasets.

## 88. Post-It Note Sort

- **Algorithm:**
  - Humorous and impractical sorting algorithm.
  - Involves physically rearranging post-it notes.

## 89. Incremental Quicksort

- **Algorithm:**
  - Variation of quicksort that sorts data incrementally.
  - Suitable for scenarios where data arrives progressively.

## 90. Retroactive Sorting

- **Algorithm:**
  - Sorting strategy that allows for the insertion and removal of elements after sorting.
  - Adapts to dynamic changes in the dataset.

## 91. Hybrid Comb QuickSort

- **Algorithm:**
  - Combines principles of comb sort and quicksort.
  - Aims to provide a balance between the strengths of both algorithms.

## 92. Bidirectional Shell Merge Sort

- **Algorithm:**
  - Merges principles of bidirectional shell sort and merge sort.
  - Elements are sorted using both bidirectional shell sort and merge sort.

## 93. Logarithmic Merge Sort

- **Algorithm:**
  - Variation of merge sort with logarithmic time complexity.
  - Adapts principles to reduce the number of comparisons.

## 94. Block Merge Sort

- **Algorithm:**
  - Sorting algorithm that processes elements in blocks.
  - Particularly efficient for data stored in blocks of memory.

## 95. Juggle Sort

- **Algorithm:**
  - Sorting technique based on rotation.
  - Elements are moved cyclically until the list is sorted.

## 96. Remote Inversion Sorting

- **Algorithm:**
  - Sorting strategy inspired by remote inversions.
  - Utilizes inversion operations for sorting.

## 97. Tournament Merge Sort

- **Algorithm:**
  - Merges principles of tournament sort and merge sort.
  - Implements a tournament-style comparison for sorting.

## 98. Exponential Sort

- **Algorithm:**
  - Sorting algorithm with an exponential growth pattern.
  - Elements are repeatedly divided into subgroups for sorting.

## 99. Dynamic Radix Sort

- **Algorithm:**
  - Variation of radix sort adapted for dynamic datasets.
  - Efficient for sorting elements with varying numbers of digits.

## 100. Teleportation Sort

- **Algorithm:**
  - Humorous and impractical sorting algorithm.
  - Involves teleporting elements to their sorted positions.

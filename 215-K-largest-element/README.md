## Idea

### 1. Sort

This is quite simple, we sort the whole array, which costs `O(nlgn)`. 

### 2. Min Heap

build a min heap, and we keep track of the k-th largest elements. then
we just pop the smallest value of this heap

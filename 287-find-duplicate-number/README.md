## Proof

Proving that at least one duplicate must exist in nums is simple application of the pigeonhole principle. Here, each number in nums is a "pigeon" and each distinct number that can appear in nums is a "pigeonhole". Because there are `n+1` numbers are nn distinct possible numbers, the pigeonhole principle implies that at least one of the numbers is duplicated.

## Idea

_Note_: 

1.we can not modify the array: it seems we can not use the same trick in [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/) and [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)
2.we must use `O(1)` space: can not buld a _Hash Table_ such as `dic[num] = # of appear`
3.time complexity less than `O(n^2)`: can not compare `elem` by `elem`. 
4.one duplicate number in the array, but it could be repeated more than once: can not use the trick in [268. Missing Number](https://leetcode.com/problems/missing-number/description/) 

So what should we do?

### Intuition

we can reduce this problem to cycle detection.

### Algorithm

First off, we can easily show that the constraints of the problem imply that a cycle must exist. Because each number in `nums` is between `1` and `n`,  it will necessarily point to an index that exists. Therefore, the list can be traversed infinitely, which implies that there is a cycle. Additionally, because `0` cannot appear as a value in `nums`, `nums[0]` cannot be part of the cycle. Therefore, traversing the array in this manner from `nums[0]` is equivalent to traversing a cyclic linked list. Given this, the problem can be solved just like [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/).
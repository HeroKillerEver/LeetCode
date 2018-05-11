## Idea

### 1. Hash Table

This comes quite natural, we build a hash table to store the `num` and the `time` it appears:

```python
dic[num] = '#'  
```

this takes `O(n)` time and `O(n)` space

### 2. Stack

This idea is a little bit hard to come with, I will explain as simple as I can. Since we know
there must be an element which appears more than `n/2`. So it is like if we compare `2` number, 
if they are the same, we just add them to our stack (the stack is to save for the candidate number)
if they are different, we just remove this `2` numbers.

Note since there is one element greater than `n/2`, even though we remove `2` numbers, the remaining number
is just the candidate we are looking for. 

> this takes `O(n)` time and `O(n)` space


### 3. Boyer-Moore Voting Algorithm

The idea is similar to [Stack](### 2. Stack)

> this takes `O(n)` time and `O(1)` space


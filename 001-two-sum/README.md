## Idea

-----------


The idea to solve this problem is quite simple, we need to output a pair of `a, b` such that `a + b = target`. 
So we just build a hash table (dictionary) to save all the nums and their index we have seen so far, which to be said:

```
dic[num] = idx
```

when `target - b` is in dic, then we just return the index
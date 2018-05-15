## Idea

1. _Brute Force_

 quite easy to think of, time limit exceed

2. _Hash Table_

 we build up a hash table where

 ```python
 dic[current number] = current location
 ```

 Since we don't really care about the pervious locations since it does not satisfy the condtion. when the `next element` is in the hash table, we just compare `previous location` and `current location` to make sure whether `current location` - `previous location` <= `k`. 

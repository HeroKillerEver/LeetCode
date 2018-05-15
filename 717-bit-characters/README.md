## Idea

1.My idea is pretty simple, since we encounter `1`, we just pop out `1 + 'x'`, if we encounter `0` 
we just pop `0` itself, if the remaining `bits == [0]`, then it means we get the correct answer.  

_Note_: the `pop(0)` takes `O(n)` time,  hence this algothm takes `O(n^2)` time and `O(1)` space

2.A natural idea to think is to represent `bits` using a queue `bits_queue`, since `bits_queue.popleft()` takes `O(1)` time. 

_Note_: this algorithm takes `O(n)` time and `O(n)` space

3.We just create a flag `length` to illustrate how many digits we have already passed, if we encounter
`1`, then `length += 2`, else `length += 1`. finally we compare `length = len(bits)-1` .  

_Note_: this algothm takes `O(n)` time and `O(1)` space
## Idea

This problem is a little bit hard to think at first. But when you write down for a few samples, you wiil discover the patterns inside them, let us get started:

if `n = 0`: `0 -- 0`

if `n = 1`: `0 -- 0`, `1 -- 1`

if `n = 2`: `00 -- 0`, `01 -- 1`, `11 -- 3`, `10 -- 2`

if `n = 3`: `000 -- 0`, `001 -- 1`, `011 -- 3`, `010 -- 2`, `110 -- 6`, `111 -- 7`, `101 -- 5`, `100 -- 4`. 

Did you find out the pattern,  we denote the result as `f(n)`, it is just like:
> f(n) = \[0, f(n-1)\] + \[1, reverse(f(n-1))\]
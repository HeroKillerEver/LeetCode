## Idea

Actually this problem took me sometime to think about, finally I realized that the value of `()` represents depends on how many `(` it encountered before it closes the parentheses by `)`. For example,

`(((())))`, as we know this one represents `8`, we find out that it encounters `4` `(` before `)`. then we have 
```
8 = 2^(4-1) = 2^(# of '(' - 1)
```
So we know that when we encounter `(`: `layer += 1`, when we encounter `)`: `layer -= 1`. 

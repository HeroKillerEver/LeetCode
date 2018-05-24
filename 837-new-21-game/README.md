## Idea

This problem shares some similarity w.r.t Fib numbers. 

we denote `dp[i]` as the probability of geting points `i`, so we know to achieve `dp[i]`, we can draw `1` from `dp[i-1]`, `2` from `dp[i-2]`, `......`, `W` from `dp[i-W]`,  and we know that the probability of drawing `1,2,3, ..., 10` is equal and they are `1/W`. So we can write the equation as:
```bash
dp[i] = 1/W * (dp[i-1] + ... + dp[i-W])
```

_Note_: corner case need to be considered, initial state and when `dp[i]` reaches `K`
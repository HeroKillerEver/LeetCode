## Idea

Given a positive interger `N` if it can be written as a sum of consecutive positive integers, then the maximum number could be:
```
1 + 2 + ...... + k = N
```
So the maximum `K = ceil(0.5 * (-1 + sqrt(8*N)))`. Then the possible number would be from `1` to `K`.
Then for a given `k` within `[1, K]`:
```
m + m+1 + ...... + m+k-1 = N
m = (2*N - k**2 + k) / (2*k)
```
`m` must be an `int`. We just check `m == int(m)` for a given `k` 
## Idea

At the first glance, I don't think we should solve this problem by using reflection. then I just inspect the problem, it seems the init speed is like `(p, q)`, so after `k` steps, we should reach `(kp, kq)` without blocking. Since now we are in this square, `0` represents `(p, 0)`, `1` represents `(p, p)`, 2 represents `(0, p)` which we can rephrase `0` as x-distance is `1` more length than y-distance,  `1` as x-distnace same as y-distance and `2` as y-distance is `1` more than x-distance. 

Let us check point `(kp, kq)`, if it stops which means that `kq = mp`. So we know that `kq = mp = lcm(p, q)`. then we know `k = lcm(p, q) / q = p / gcd(p, q)` and `m = lcm(p, q) / p = q / gcd(p, q)`, so finally we get `(kp, mp)`. the meeting point should be `(k%2, m%2)`

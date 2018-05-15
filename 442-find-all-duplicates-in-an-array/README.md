## Idea

I think it is quite easy to come up with an `O(n)` time complexity and `O(n)` space complexity algorithm.
where we just build a set called `seen` to keep track of those elements we have already seen. Then:

```python
if elem in seen: out.append(elem)
```

But for `O(n)` time complexity and `O(n)` space complexity algorithm, it is quite convoluted. Note we have
2 properties could use:
> elem is positive
> their range is between (1, n)

So it is possible every time we encounter an `elem`, we just set `nums[elem] *= -1` to make it negative. And next time if we encounter `elem` again, we could use whether `nums[elem]` is `+` of `-` to tell whether we encountered it previously. if `nums[elem] < 0`, then `elem` is a repeated element.

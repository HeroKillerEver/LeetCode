## Idea

The key idea to sort the traget string `T` is to base on their weight appeared in the source string `S`:

```python
dic[string] = weight (in S)
```
And for the `string`  which does not appear in `S`,  we could sort them according to their ASCII number.
Since `len(S) <= 26`, so maximum `weight <= 26`. which are always smaller than ASCII number.  
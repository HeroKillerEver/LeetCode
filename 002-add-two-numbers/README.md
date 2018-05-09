## Idea

The idea to solve this problem is to loop over the two lists

```
node1, node2, node3, node4
node1, node2, node3, node4
|
```

The most tricky part is to keep track of the `carry` flag which is:
```
c = a + b + carry
carry, c = c // 10, c % 10
```

Don't foget to check whether **carry** after traversing



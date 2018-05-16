## Idea

First, to check if information is an email, we check whether it contains a `@`. (There are many different tests: we could check for letters versus digits, for example.)

If there is no `@` character, then we just check whether:

```
digits = ''.join([item for item in S if item.isdigit()])
len(digits) == 10
```

to see whether the numbe is local or international
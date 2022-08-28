# Question | "Red@cted"

When you want to keep parts of you messages private you **redact** them. That means hiding some of the text with symbols.

You need to define a function called ``redact`` that takes two arguments: ``text`` and ``secret``.

The function should return the text with the secret redacted and replaced with a # *(a hash symbol)*. For example:

```
print(redact('I hid the gold in the park.', 'park'))
```

```
I hid the gold in the #.
```

Here's another example:

```
print(redact('The key is near, get the key!', 'key'))
```

```
The # is near, get the #!
```

## Testing your function
We've given you an ``if`` ``__name__ == '__main__'``**:** block. Any code inside this ``if`` statement **will not** affect the marking.

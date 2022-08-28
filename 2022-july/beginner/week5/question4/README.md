# Question | "I Spy The Spy!"

In spy movies the secret agent sometimes has a special coded message they use to identify themselves.

Define a function — ``spy_time`` — that works out if someone is a spy or not. It takes two arguments: ``name`` and ``message``.

Your function should check if the name is a substring of the message, and let you know whether the message identifies a spy or not.

For example, if the name is "***bond***" and the message is "family ***bond***ing time", your function should return:

```
print(spy_time('bond', 'family bonding time'))
```

```
bond is a spy.
```

If the name isn't hidden in the message your function should work like this:

```
print(spy_time('maria', 'I am a spy'))
```

```
No spy here.
```

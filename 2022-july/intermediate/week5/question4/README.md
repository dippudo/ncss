# Question | "Secret Chat"

A friend has just sent you a secret message, made of seemly randomly jumbled letters.

You know that it's a substitution cipher... a type of code where each letter is replaced by a different English letter, and you already have the key to decode it.

The file ``substitution.txt`` contains the substitutions used, with the normal alphabet on the left, and substitutions on the right.

When a message is written using this type of code, spaces and punctuation remain the same.

For example:

```
Secret Message	  Translation
WGN KWGYG	  HEY THERE
```

Write a program to decode messages **from** the cipher into plain english. Your program should ask for a cipher and then convert it to English.

Here's an example of how your program should look:

```
Secret Message: R HGGO KF KGEE NFA JFIGKWRHL RIZFYKSHK
Translation: I NEED TO TELL YOU SOMETHING IMPORTANT
```

Here's another example:

```
Secret Message: IN BSK RJ RHBYGORCEN BAKG!
Translation: MY CAT IS INCREDIBLY CUTE!
```

And here are two more secret messages to test your code on:

```
JGBYGK - KWSK BEFAO EFFVJ ERVG S KYFICFHG :F
```

```
AYLGHK - TG'YG YAHHRHL FAK FU IREV
```

**While testing your code, we'll only use messages that have characters in** ``substitution.txt`` **(and spaces).**

# Question

A local community group is painting a mural and wants to make sure they have enough tins of paint in their store room.

Ask volunteers to record the colour of the tins of paint and how many of that colour they found.

They need to make sure they have enough blue paint for the expansive sky in their design.

If the paint colour label **contains the string** 'blue' with any capitalisation, your program should say:

```
Which colour did you find? Cerulean Blue
Number of tins: 8
Excellent! We'll soon have enough paint for the sky!
```

Here's another blue record:
```
Which colour did you find? eLeCtRiC bLuE!
Number of tins: 2
Excellent! We'll soon have enough paint for the sky!
```

For a non-blue paint colour with a count **fewer than 4** it should say:
```
Which colour did you find? ANDROID GREEN
Number of tins: 3
We're running out of android green paint. Let's restock!
```

**Note:** the paint colour name is all lowercase in the output!

For any other situation, it should say:
```
Which colour did you find? french lime
Number of tins: 107
Great! We have 107 tins of french lime paint.
```

**We won't test your program with fewer than 2 tins of paint counted.**

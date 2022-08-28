# Question | "Animal Antics"

We've written a function ``animal_power`` which takes an animal (a string) and returns their power level. For example, ``animal_power('Kangaroo')`` gives a power rating of ``102``.

Write a program that asks for two animals, then uses ``animal_power`` to see which animal would win in a battle, like this:

```
Animal 1: Kangaroo
Animal 2: Crocodile
Animal 1 wins!
```

1. Ask for two teams and store them in two variables:

```
Animal 1: Kangaroo
Animal 2: Crocodile
```

2. Call ```animal_power``` to get the powers of each animal. Remember to save the result in two new variables.

3. Compare the two animals' **powers** to find out which message to print (use the powers, not the animal names).

If animal 1's power is greater than animal 2's print: ``Animal 1 wins!``

If animal 2's power is greater than animal 1's print: ``Animal 2 wins!``

If they're equal, print: ``A tie!``

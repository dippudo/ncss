# Question | "Craft Work"

CraftWork is a game where you can craft things out of different materials. You collect ore, and can convert the ore into iron to craft different objects.

Write a program to take in the amount of ore collected, and print out the object you can create that uses the most iron.

For example:
```
Ore: 51
19.6 Iron - Pickaxe
```
Another example:
```
Ore: 12
4.6 Iron - Useless lump
```

Finish the calculate_iron function we've started for you to convert the ore into iron, rounding to 1 decimal place. Use this function when you write the rest of your code.

**Use the formula below for your conversion:**
*Iron = Ore * 5/13*

Your program should print out the items your can craft from the table below:
```
Iron        Item
<5 Iron	    Useless lump
5 - <20	    Pickaxe
20 - <35    Sword
35 - <45    Fancy shield
≥45	    Magic amulet
```

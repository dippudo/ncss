# Question | "A Menagerie of Meals"

You've decided to learn to cook more. There are lots of recipes out there, so you decide to ask your friends for recommendations.

Write a program to help track the recipes to watch. Your program should ask for a friend's name and a recipe they recommend, until 5 different recipes are suggested. *Each recipe cannot be recommended more than once.*

Once 5 different recipes have been suggested, it should print the list of recipes and the friends who recommended them. Here's an example of how the program should look:

```
Friend: Jayden
Which recipe did they recommend? Spanakopita
Jayden recommended Spanakopita!
Friend: Lily
Which recipe did they recommend? Bacon and eggs
Lily recommended Bacon and eggs!
Friend: Vanessa
Which recipe did they recommend? Rotkohl
Vanessa recommended Rotkohl!
Friend: Jayden
Which recipe did they recommend? Laksa
Jayden recommended Laksa!
Friend: Ali
Which recipe did they recommend? Pizza
Ali recommended Pizza!
Cookbook complete! Recipes include:
Spanakopita: recommended by Jayden
Bacon and eggs: recommended by Lily
Rotkohl: recommended by Vanessa
Laksa: recommended by Jayden
Pizza: recommended by Ali
```

***Note:** Friends are allowed to recommend more than one recipe.* In this example, Jayden recommended both Spanakopita and Laksa.

Here's another example, where someone suggests a recipe that has already been recommended. The program prints: ``Someone else already recommended that.``

```
Friend: Nick
Which recipe did they recommend? Dumplings
Nick recommended Dumplings!
Friend: Lily
Which recipe did they recommend? Soy sauce eggs
Lily recommended Soy sauce eggs!
Friend: Max
Which recipe did they recommend? Dumplings
Someone else already recommended that.
Friend: Max
Which recipe did they recommend? 2 minute noodles
Max recommended 2 minute noodles!
Friend: Ella
Which recipe did they recommend? Poke bowl
Ella recommended Poke bowl!
Friend: Jono
Which recipe did they recommend? Chicken Parmie
Jono recommended Chicken Parmie!
Cookbook complete! Recipes include:
Dumplings: recommended by Nick
Soy sauce eggs: recommended by Lily
2 minute noodles: recommended by Max
Poke bowl: recommended by Ella
Chicken Parmie: recommended by Jono
```

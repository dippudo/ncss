# Question | "Hide And Zombies"

You're playing hide and seek, looking for your friends. Once you find a friend, they turn into a zombie!

We've given you a list called ``friends``, which contains the names of the friends you need to find.

Write a program to keep track of the game! It should ask for the name of the friend you've just found.

If they're in the list, it should replace their name in the list with ``'Zombie'``, and print their name, followed by ``'has turned into a zombie!'``.

If they aren't in the list, it should leave the list unmodified and print a message saying ``'Everyone is still in the game'``.

Here's an example of how your program should look:

```
Friends: Nicola, Penny, Dom, Nathan, Josie
Who did you find? Penny
Penny has turned into a zombie!
Remaining players: Nicola, Zombie, Dom, Nathan, Josie
```

Here's an example where an inputted name isn't on the list:

```
Friends: Nicola, Penny, Dom, Nathan, Josie
Who did you find? Bruce
Everyone is still in the game!
Remaining players: Nicola, Penny, Dom, Nathan, Josie
```

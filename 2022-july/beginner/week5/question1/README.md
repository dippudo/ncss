# Question | ""

In the Olympics, [Taekwando](https://en.wikipedia.org/wiki/Taekwondo_weight_classes#Olympic_weight_classes) competitors are broken up into classes by weight. This is the table for female competitors:

```
Max Weight (kg)		Class
Unlimited		Heavyweight
67			Welterweight
57			Featherweight
49			Flyweight
```

We've written a function to sort competitors into the correct classes.

1. Run the program without changing it and try to figure out what's going wrong.

2. Change the first line of the if statement to be > instead of < and run it again.

3. There's one more bug: let's add a test to find it. Print ``weight_class(55)`` and run it to see what goes wrong. (You can add tests at the bottom of the program, below the red comment)

4. Inside the function, fix the bug: add another ``elif`` statement to include the missing weight class Featherweight.

Then try marking your code 🤞.

## Testing your function
An ``if`` ``__name__ == '__main__'``**:** block is already there. Any code inside this ``if`` statement **will not** affect the marking. You can add more tests to the end of this.

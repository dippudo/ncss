# Question | "A Place to Call Home"

You can find many examples of [tessellation](https://en.wikipedia.org/wiki/Tessellation) in nature!

We love bees! Let's make some tessellating honeycomb cells as a home for them.

We've written some code to draw a honeycomb for the bees, but we need a function to draw each individual hexagon.

Our code will call the function to draw each hexagon in the honeycomb, and say what position and colour it should have.

1. Create a function called ``draw_hexagon`` that takes three arguments:

* ``x`` – the x-coordinate to move to
* ``y`` – the y-coordinate to move to
* ``colour`` – the colour to fill the tile with 

2. Start the function. The turtle should move to the ``x`` and ``y`` coordinate *without* drawing anything.

3. Get ready to draw the hexagon:

* Put the ``pen down``;
* Set the ``fillcolor`` to the correct ``colour``;
* Begin the fill.

4. Continue the function. It should draw a hexagon:

* With six sides of length ``30`` and;
* With six ``right`` turns of ``60`` degrees.
* Your hexagon should start by going ``forward`` and finish by turning ``right``.

*Remember to put the pen down before drawing!*

**If an inside angle of a hexagon is 120°, then the outside angle the turtle needs to turn is 180° - 120° = 60°.**

5. Remember to include ``end_fill()``.

# Question | "Sketchy Snowflake"

We're going to draw a snowflake, made up of branches.

We've provided you with a function that draws one branch. We'll use a loop to see how the pattern looks with different numbers of branches.

1. Set the pen size to ``2``, the fill colour to ``'white'``, the pen colour to ``'white'`` and the background colour to ``'darkblue'``.

2. Ask the user ``'How many branches? '``, and save it to a variable. Don't forget to save it as an ``int``!

3. We want to arrange the branches with equal space between them and such that they are drawn in a circle. To do this we need to use this formula and store the answer in a variable for later:

*angle = 360 / number of branches*
 
4. Begin the fill.

5. Time to draw! Make a ``for`` loop using the number of branches and ``range``. It will be very similar to the previous question.

Now, inside the ``for`` loop, call ``draw_branch`` and turn right by the angle you calculated with the formula above.

6. Finish off the snowflake by ending the fill **outside** the ``for`` loop.

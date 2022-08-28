# Question | "Olympic Occasion"

We're looking forward to the next Olympics and are designing some fireworks in the colours of the [Olympic rings](https://en.wikipedia.org/wiki/Olympic_symbols)!

Create a function that draws a single firework called firework with 3 parameters: ``colour``, ``x`` and ``y``. Use it to draw the 4 coloured fireworks over the sky!

1. Use ``def`` to define a function called firework. It should take three parameters: ``colour``, ``x`` and ``y``.

2. Inside the function start by setting the ``pensize`` to ``4`` and the ``pencolor`` to the ``colour`` parameter.

3. Move to the coordinates (0, -150) without drawing anything. It's a great spot to launch our fireworks from!

4. Launch the firework! Draw a line to the coordinates ``x`` and ``y`` (the parameters of your function) using ``goto``.

5. Draw the explosion! Create a ``for`` loop using ``range`` to draw ``10`` lines. Inside your loop you should move ``forward`` and ``backward`` ``50`` steps, then turn ``36`` degrees.

6. We've already called the function to draw the blue and green fireworks. Use the function to draw the final two fireworks:

* An **Olympic Yellow** firework with hex colour ``'#F4C300'`` at coordinates (-50, -40)
* An **Olympic Red** firework with hex colour ``'#DF0024'`` at coordinates (40, -60)

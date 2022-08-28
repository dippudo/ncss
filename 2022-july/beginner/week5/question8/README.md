# Question | "Pinwheels"

Let’s draw a colourful [pinwheel](https://en.wikipedia.org/wiki/Pinwheel_(toy)).

Define a function called wheel with three parameters: ``red``, ``green``, and ``blue``. We'll use these as the RGB values for our wheels.

By changing just the red value in between drawing each vane of the wheel, we can create some cool colour gradients, like this:

1. Define a function called ``wheel``, with three parameters: ``red``, ``green``, and ``blue``.

2. Inside the function, set up a ``for`` loop to repeat for each of the ``12`` vanes of the pinwheel. The rest of our function code will go inside the loop.

3. Set the fill colour to an RGB colour, using the ``red``, ``green``, and ``blue`` parameters.

4. Now, let's get into position! Turn left ``30`` degrees and begin the fill for the vane. We want to begin fill, draw the vane, and then end fill.

5. Draw the vane (which is the shape of a diamond)! Each side is ``50`` steps long. You'll need to turn right ``60`` degrees to draw the angle on each side of the diamond, and ``120`` degrees to draw the point at the top of the wheel. Once you've drawn all four sides, end the fill.

6. To get into position for the next vane of the pinwheel, you will need to turn right ``180`` degrees and move forward ``20`` steps.

7. Finally, let's change the red value so that the next vane of the pinwheel will be a slightly different colour. We'll subtract 20 from the value like this: ``red = red - 20``

8. Run the code to see how your pinwheel looks! Change the values in the function call to try out some different colours.

**N.B. The** ``red`` **value needs to be at least** ``220``**.**

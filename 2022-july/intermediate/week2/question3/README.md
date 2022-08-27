# Question | "Prezzie Packaging"

Your friend is making gift boxes in a range of different heights and would like some help to calculate their volumes.

All the boxes will be prism shaped, so you can use the formula:

*Volume = base * height*

Write a program that asks for the area of the base (this will be a whole number in cm² units) and then prints the volumes of the gift boxes in a range of heights.

The smallest height that your friend can make the gift boxes is 10 cm and the largest height possible is 20 cm.

Your program should also ask for a step number, and increase the height by that much each line.

For example, if the step number is 1, then the volume for every height from 10 to 20 is printed, like this:

```
Area of base: 100
Step: 1
Height: 10 cm, Volume: 1000 cm³
Height: 11 cm, Volume: 1100 cm³
Height: 12 cm, Volume: 1200 cm³
Height: 13 cm, Volume: 1300 cm³
Height: 14 cm, Volume: 1400 cm³
Height: 15 cm, Volume: 1500 cm³
Height: 16 cm, Volume: 1600 cm³
Height: 17 cm, Volume: 1700 cm³
Height: 18 cm, Volume: 1800 cm³
Height: 19 cm, Volume: 1900 cm³
Height: 20 cm, Volume: 2000 cm³
```

If the step number is 4, then the volumes for heights of 10, 14 and 18 are printed, like this:

```
Area of base: 25
Step: 4
Height: 10 cm, Volume: 250 cm³
Height: 14 cm, Volume: 350 cm³
Height: 18 cm, Volume: 450 cm³
```

Your program should work for any whole number base area or step number greater than 0.

# Question | "Walk-a-thon"

Your school is doing a walk-a-thon to get more people moving! Each participant will use a wearable device to log how many kilometres they walked. A list will be formed at the end so that they can recieve a merit certificate for participating.

Write a program that will help keep track of your school's participants and how far they walked overall as a total.

Write a program that will track student participation and the total walking distance for the school.

Your program should keep asking for participant names until nothing is entered. When a name is entered, ask for how far they walked, update the total distance in kilometres, record the participant name if this is their first entry, and acknowledge their achievement!

When all the entries are recorded, print out the total distance walked. Then, print out all the participant names in **alphabetical** order with a medal symbol (🏅).

Here's an example of how your program should work:

```
Let's start the walk-a-thon!
Who has recorded a walk? Sarah
How far did they walk? 4.3
That's a first time for Sarah! They walked 4.3 km!
Who has recorded a walk? Divyesh
How far did they walk? 9.3
That's a first time for Divyesh! They walked 9.3 km!
Who has recorded a walk? Sarah
How far did they walk? 3.82
Another walk from Sarah. Well done on another 3.82 km!
Who has recorded a walk? 
Thanks for taking part in the walk-a-thon! We walked a total of 17.42 km!
Here is a list of merit certificate winners:
🏅 Divyesh
🏅 Sarah
```

Here's a longer example:

```
Let's start the walk-a-thon!
Who has recorded a walk? Daniel
How far did they walk? 7.4
That's a first time for Daniel! They walked 7.4 km!
Who has recorded a walk? Ana
How far did they walk? 10
That's a first time for Ana! They walked 10.0 km!
Who has recorded a walk? Daniel
How far did they walk? 2.3
Another walk from Daniel. Well done on another 2.3 km!
Who has recorded a walk? Priya
How far did they walk? 5.8
That's a first time for Priya! They walked 5.8 km!
Who has recorded a walk? Ana
How far did they walk? 9.7
Another walk from Ana. Well done on another 9.7 km!
Who has recorded a walk? 
Thanks for taking part in the walk-a-thon! We walked a total of 35.2 km!
Here is a list of merit certificate winners:
🏅 Ana
🏅 Daniel
🏅 Priya
```

***Note**: At the end when no name is entered, it doesn't ask for distanced walked. Be careful where you put your second ``input``.*


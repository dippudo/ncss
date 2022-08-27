# Question | "Intergerian Conflict"

You are 255, loyal subject of the Monarch Pentad. In their domain are all multiples of 5, but a war with King Minus looms, and the Pentadian kingdom needs to bolster its numbers.

Your Monarch has tasked you to perform a survey to count all **free numbers** - numbers that belong to no domain.

There are 4 domains:

```
Pentadian	   Numbers divisible by 5.
Minutian	   Numbers less than 0.
Disiphine	   Numbers containing the digit 2.
Primean	Numbers    in the list primeans.
```

Your program should ask for a list of space-separated numbers. For any number belonging to at least one domain, it should print its full citizenship, with domains listed in the same order as the table above. Then, it should print how many free numbers were counted.

Here's an example:

```
Enter numbers: 11 4 378 -7 -420 55
11 is a Primean citizen.
-7 is a Minutian citizen.
-420 is a Pentadian Minutian Disiphine citizen.
55 is a Pentadian citizen.
Free numbers: 2
```

*Note how ``4`` and ``378`` weren't printed out, because they didn't belong to a domain. They were counted as **free numbers** instead.*

**To break up the task use a function that helps find the domains of numbers.**

We’ve started a ``check_domain`` function for you. But so far it only checks if the number is Pentadian. Finish the function by adding checks for the other domains, then use it in your program.

Here are some examples of what your function ``check_domain`` should output:

```
Input		        Output
check_domain(12)	'Disiphine '
check_domain(575)	'Pentadian '
check_domain(521)	'Disphine Primean '
check_domain(-205)	'Pentadian Minutian Disiphine '
check_domain(86)	''
```

``86`` is a free number, so it returns an empty description.
Numbers from domains have spaces at the end.

Here's one more example of how your program should work:

```
Enter numbers: 8 -225 510 23 377 91
-225 is a Pentadian Minutian Disiphine citizen.
510 is a Pentadian citizen.
23 is a Disiphine Primean citizen.
Free numbers: 3
```

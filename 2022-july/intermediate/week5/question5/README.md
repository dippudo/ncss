# Question | "Catchy Carols"

It's not even remotely close to December but you've got catchy Christmas carols stuck in your head. Let's write a program to adapt the carol lyrics to celebrate a different holiday!

You have several **carol lyrics files** which contain the original lyrics of the carol.

You also have some **replacement word files** which contains pairs of original and replacement words. Each row has the original word then the word that will replace it in the new song lyrics, separated by a space. The words in this file will be lowercase.

Your program should ask for the name of the name of a file that contains the carol lyrics, then for the name of a file that contains the replacement word pairs.

Then, it should print an empty line, then the new song title in uppercase, and then the lyrics of the new song.

The title of the song should be in uppercase, with MY, the holiday or theme that replaces christmas, then SONG!.

The lyrics of the new song will have the christmas words replaced with more relevant words. The replacement word in the new lyrics should be the same case as the original word (for lower, upper and title case*).

**Here are some examples of how your program should work:**

Here's an example using the replacement words in ``replace_halloween.txt`` on a snippet of Jingle Bells from the ``short_jingle_bells.txt`` file:

```
Filename of carol lyrics: short_jingle_bells.txt
Filename of replacement words: replace_halloween.txt

MY HALLOWEEN SONG!
Dashing through the streets
In a one-horse open pumpkin
```

And another example on a snippet of a different carol:

```
Filename of carol lyrics: short_christmas_tree.txt
Filename of replacement words: replace_halloween.txt

MY HALLOWEEN SONG!
O Halloween tree O Halloween tree
How are thy leaves so withered
```

**We've started off some functions to break the problem down:**

*Finish the functions & use them to write the rest of the program.*

* ``get_replacements`` - Turn a file of pairs of original and replacement words into a dictionary.

* ``convert_word`` - Turns a word from the original lyrics into the word that will be used in the new song.

* ``convert_line`` - Turns a whole line from the original lyrics into the line that will be used in the new song. This requires the *``convert_word``* function.

* ``print_new_song`` - Reads in the original carol lyrics and prints out the new song. This requires the *``convert_line``* function.

Here are some example calls to the first three functions:

```
>>> get_replacements('short_replace.txt')
{'christmas': 'halloween', 'snow': 'streets', 'sleigh': 'pumpkin'}
>>> convert_word('SNOW', {'snow': 'streets'})
'STREETS'
>>> convert_line('Dashing through the snow\n', {'snow': 'streets'})
'Dashing through the streets'
```

**We'll test your code with the files provided and some new files too.**

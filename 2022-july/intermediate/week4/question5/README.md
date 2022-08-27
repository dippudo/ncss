# Question | "DAngerous Mafia"

You're playing the coolest new game, Dangerous Mafia. The aim of the game is to collect skins on all your items!

The way to get skins is to buy them with the game's token, DAM. You earn DAM by winning games, but you can also lose DAM by losing games. Damn!

## Start the game
Print the start message. Then, ask for friends' names and how many DAM tokens they're starting with, until a blank name is entered. You'll need to keep track of all of the players and their starting amounts.

## Print the player names
Print out each name and how many skins they can buy with their starting amount.

## Buying skins
We've started a ``buy_skins`` function for you. Each skin costs **40 DAM**, but you can only buy a *whole number* of skins. This means you'll need to *round down*.

## Play some games
Ask for the player name, then how many DAM they won or lost in that game. Keep going until a blank name is entered.

## Wrap it up
Print a list of every player and how many skins they can buy at the end.

## Examples
**Watch out!** Games can cost DAM to play, so people will *lose* DAM if they don't win!

```
Who's playing Dangerous Mafia?
Name: Lisette
Starting number of DAM: 450
Lisette's here, starting with 11 skins worth of DAM!
Name: Bruce
Starting number of DAM: 60
Bruce's here, starting with 1 skins worth of DAM!
Name: 
Let's play!
Who played? Lisette
DAM won/lost: 110
Who played? Lisette
DAM won/lost: -60
Who played? Bruce
DAM won/lost: 30
Who played? 
End of the game! Let's see how everyone did!
Lisette can buy 12 skins.
Bruce can buy 2 skins.
```

*In the second game, Lisette lost 60 DAM, so the input was -60.*

Friends can join after the beginning of the game. If someone enters a name **not** in your dictionary, *assume they start with 0 tickets*, and add whatever they've just won:

```
Who's playing Dangerous Mafia?
Name: Jack
Starting number of DAM: 130
Jack's here, starting with 3 skins worth of DAM!
Name: 
Let's play!
Who played? Jack
DAM won/lost: -50
Who played? Katelynn
DAM won/lost: 38
Who played? Katelynn
DAM won/lost: 110
Who played? 
End of the game! Let's see how everyone did!
Jack can buy 2 skins.
Katelynn can buy 3 skins.
```

**Note:** We won't give you any inputs that lead to someone having *negative* total tickets at any time.

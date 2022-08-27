def buy_skins(dam):
   # Finish the function to convert DAM to skins
  skins = int(dam/40)
  return skins

# Write the rest of your program here
players = {}

print("Who's playing Dangerous Mafia?")

name = input("Name: ")

while name != "":
  startingDam = int(input("Starting number of DAM: "))
  players[name] = startingDam
  
  starting_skins_worth = buy_skins(startingDam)
  
  print(f"{name}'s here, starting with {starting_skins_worth} skins worth of DAM!")
  
  name = input("Name: ")

if name == "":
  print("Let's play!")


namePlayed = input("Who played? ")

while namePlayed != "":
  won_lost = int(input("DAM won/lost: "))
  damAfterPlay = players.get(namePlayed, 0) + won_lost

  players[namePlayed] = damAfterPlay

  namePlayed = input("Who played? ")

if namePlayed == "":
  print("End of the game! Let's see how everyone did!")

for player, dam in players.items():
  end_skins_worth = buy_skins(dam)

  print(f"{player} can buy {end_skins_worth} skins.")

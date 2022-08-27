players = ['Nicola', 'Penny', 'Dom', 'Nathan', 'Josie']

playersJoin = ", ".join(players)
print(f"Friends: {playersJoin}")

find = input("Who did you find? ")

if find in players:
  print(f"{find} has turned into a zombie!")
  
  position = players.index(find)
  players[position] = "Zombie"
  playersJoin = ", ".join(players)

  print(f"Remaining players: {playersJoin}")

else:
  print("Everyone is still in the game!")
  print(f"Remaining players: {playersJoin}")

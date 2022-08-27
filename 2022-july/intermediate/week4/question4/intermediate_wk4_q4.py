scoreboard = {}

player = input("Player: ")

while player != "":
  score = int(input("Score: "))
  
  if player in scoreboard:
    scoreboard[player] = scoreboard[player] + score
  
  else:
    scoreboard[player] = score

  player = input("Player: ")

print("Final Results:")

for player, score in scoreboard.items():
  print(f"{player}: {score}")

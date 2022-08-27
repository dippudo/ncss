area = int(input("Area of base: "))
step = int(input("Step: "))

for height in range(10, 21, step):
  volume = area * height
  print(f"Height: {height} cm, Volume: {volume} cm³")

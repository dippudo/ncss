city_file = input("Enter a city file: ")
print("And the nominees are...")

birds_list = []

with open(city_file) as city:
  
   for bird in city:
    bird = bird.strip()
    
    if bird not in birds_list:
      birds_list.append(bird)
      
    elif bird in birds_list:
      pass

birds_list.sort()

for bird in birds_list:
  print(f"🐦 {bird.strip()}")

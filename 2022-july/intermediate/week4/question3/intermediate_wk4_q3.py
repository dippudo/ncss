friends_recipes = {}
friends_recipes_count = len(friends_recipes.items())

while friends_recipes_count < 5:
  friend = input("Friend: ")
  recipe = input("Which recipe did they recommend? ")

  if recipe not in friends_recipes.keys():
    friends_recipes[recipe] = friend
    print(f"{friend} recommended {recipe}!")

  elif recipe in friends_recipes.keys():
    print("Someone else already recommended that.")

  friends_recipes_count = len(friends_recipes.items())

print("Cookbook complete! Recipes include:")

for recipe, friend in friends_recipes.items():
  print(f"{recipe}: recommended by {friend}")

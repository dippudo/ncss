cheeses = ['Cheddar', 'Bocconcini', 'Haloumi', 'Paneer', 'Gorgonzola', 'Mozzarella', 'Parmesan', 'Brie', 'Gruyere']

# Add your code after this.

word = input("Cheese: ")

if word in cheeses:
  print(f"{word} is a cheese!")
  
else:
  print(f"{word} might not be a cheese.")

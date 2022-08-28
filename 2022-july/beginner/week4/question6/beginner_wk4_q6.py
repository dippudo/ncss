# Calculate the power of an animal
def animal_power(animal):
  power = 0

  for letter in animal:
    unicode_number = ord(letter)
    power = power + unicode_number

  average_power = int(power / len(animal))
  
  return average_power

# Add your code after this.
animal1 = input("Animal 1: ")
animal2 = input("Animal 2: ")

power1 = animal_power(animal1)
power2 = animal_power(animal2)

if power1 > power2:
  print("Animal 1 wins!")

elif power2 > power1:
  print("Animal 2 wins!")

elif power1 == power2:
  print("A tie!")

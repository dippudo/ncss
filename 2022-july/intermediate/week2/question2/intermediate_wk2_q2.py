theme = input("Party theme: ")
supplies = input("Supplies needed: ")

_supplies = supplies.split()

print(f"The {theme} party is coming up soon!")
print("We will need to get...")

for item in _supplies:
  print(f"🥳 {item}")

print(f"Remember to invite your {theme} buddies!")

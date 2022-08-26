def calculate_iron(ore):
  # Calculate the Iron from Ore, to 1 decimal place
  iron = ore * (5/13)
  return round(float(iron),1)

# Write the rest of your program here
ore = round(float(input("Ore: ")),1)

iron = calculate_iron(ore)

if iron <5:
  print(f"{calculate_iron(ore)} Iron - Useless lump")
  
elif iron >=5:
  
  if iron <20:
    print(f"{calculate_iron(ore)} Iron - Pickaxe")
    
  elif iron >=20:
    if iron <35:
      print(f"{calculate_iron(ore)} Iron - Sword")
      
    elif iron >=35:
      if iron <45:
        print(f"{calculate_iron(ore)} Iron - Fancy shield")
      
      elif iron >=45:
        print(f"{calculate_iron(ore)} Iron - Magic amulet")

#personal note: follow the ranges one by one, and indent them logically

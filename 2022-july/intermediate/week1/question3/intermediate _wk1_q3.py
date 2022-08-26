def is_crowd(people):
  # Write your function here.
  if people ==3:
    print("There's a crowd here!")
  elif people >= 30:
    print("There's a crowd here!")
  elif people < 30:
    print("There's no crowd here!")
  return

# Write the rest of your program here.
number = int(input("Number of people: "))

is_crowd(number)

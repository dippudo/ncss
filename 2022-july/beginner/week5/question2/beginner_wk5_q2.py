### Write your function here
def is_safe(water):
  if water < 6.5:
    return "Too acidic!"
  elif water > 9:
    return "Too alkaline!"
   
  else:
    return "Water is safe."

###


if __name__ == '__main__':
  print(is_safe(6))
  print(is_safe(6.5))
  
  # Add more testing here.
  print(is_safe(9))

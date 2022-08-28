def weight_class(n):  
  if n <= 49:
    result = 'Flyweight'
  elif n > 49 and n <= 57:
    result = 'Featherweight'
  elif n > 57 and n <= 67:
    result = 'Welterweight'
  elif n > 67:
    result = 'Heavyweight'
  return result

if __name__ == '__main__':
  print(weight_class(100))
  print(weight_class(42))
  print(weight_class(71))
  print(weight_class(59))

  # Add your own testing after this.
  print(weight_class(49))

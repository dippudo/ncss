# Define your function here!
def spy_time(name, message):
  if name in message:
    return f"{name} is a spy."
  else:
    return "No spy here."


if __name__ == "__main__":
  # You can use this to test your function.
  # Any code inside this if statement will be ignored by the automarker.
  
  # Test the first example in the question.
  print(spy_time('bond', 'family bonding time'))

  # Test the second example in the question.
  print(spy_time('maria', 'I am a spy'))

  # You can add more tests here!
  print(spy_time('sam', 'I like to samba'))

# Define your function here!
def redact(text, secret):
  redacted = text.replace(secret, "#")
  return redacted

if __name__ == '__main__':
  # You can use this to test your function.
  # Any code inside this if statement will be ignored by the automarker.
  
  # Test the first example in the question.
  print(redact('I hid the gold in the park.', 'park'))
  
  # Test the second example in the question.
  print(redact('The key is near, get the key!', 'key'))

  # You can add more tests here!

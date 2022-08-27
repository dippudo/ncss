post = input("Post: ").split()

counter = 0

for word in post:
  if word.isupper():
    counter = counter + 1
  else:
    counter = counter

print(f"Number of angry words: {counter}")

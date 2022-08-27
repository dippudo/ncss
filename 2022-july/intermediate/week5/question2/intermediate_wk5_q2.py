password = input("Password: ")

first_word = []
valid_counter = 0

with open("book.txt") as book:
  for line in book:
    line_split = line.split()
    line_join = "".join(line)
    
    if password.lower() in line_join.strip().lower():
      first_word.append(line_split[0])
      valid_counter = valid_counter + 1

first_word_join = ("\n".join(first_word))
print(first_word_join.lower())

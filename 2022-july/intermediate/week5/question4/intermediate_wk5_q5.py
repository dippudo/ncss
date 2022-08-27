secret_message = input("Secret Message: ")

# makes the dictionary for substitution
substitution_dict = {}

with open("substitution.txt") as sub:
  for letter in sub:
    value, key = letter.split()
    substitution_dict[key] = value
    # key = deciphered 
    # value = secret

# makes list to append after deciphering
decipher_list = []

for character in secret_message:
  if character.isalpha():
    deciphered_letters = substitution_dict.get(character) # append key (deciphered) to decipher_list
    decipher_list.append(deciphered_letters)
  
  else:
    decipher_list.append(character)

decipher_list_joined = "".join(decipher_list)

print(f"Translation: {decipher_list_joined}")

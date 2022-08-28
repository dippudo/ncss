# Encrypt word with a cipher
def encrypt(word):
  if word == '':
    return '<no-input>'

  first_letter = chr(ord(word[0]) + 2)
  last_letter = chr(ord(word[-1]) + 2)
  middle = word[-2:0:-1]  # this takes the middle out of the word and reverses it
  return f'{first_letter}{middle}{last_letter}'

# Add your code after this.
person = input("Person? ")
personEncrypt = encrypt(person)
print(f"Find {personEncrypt}.")

location = input("Location? ")
locationEncrypt = encrypt(location)
print(f"They will be at {locationEncrypt}.")

password = input("Password? ")
passwordEncrypt = encrypt(password)
print(f"The password is {passwordEncrypt}.")

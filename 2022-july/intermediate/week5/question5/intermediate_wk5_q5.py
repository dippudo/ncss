def get_replacements(replacements_filename):
  # Given the name of a file containing word-replacement pairs, 
  # return a dictionary that contains these pairs. The original words should
  # be dictionary keys and the replacement words should be the values.
  replacements_dict = {}
  
  with open(replacements_filename) as replacements_file:
    
    for line in replacements_file:
      (key, value) = line.split()
      replacements_dict[key] = value

  return replacements_dict


def convert_word(word, replacements):
  # Given a single word, returns the replacement word in the same case if a 
  # replacement exists for this word. If there is no replacement, then it
  # returns the original word.
  
  
  if word.lower() in replacements:
    if word.lower() != replacements.get(word.lower()):
      converted_word = replacements.get(word.lower())

      if word.isupper():
        converted_word = converted_word.upper()
      elif word.islower():
        converted_word = converted_word.lower()
      elif word.istitle():
        converted_word = converted_word.title()
      
  else:
    converted_word = word
    
  return converted_word
  
  
def convert_line(line, replacements):
  # Given a string line and the replacements dictionary, returns the line 
  # as a string with the words changed to their replacements and a space in 
  # between each word. 
  words = line.split()
  
  for word in words:
    replacement_word = convert_word(word, replacements)
    line = line.replace(word, replacement_word)
  
  return line
  

def print_new_song(carol_filename, replacements):
  # Given the name of the file containing the carol and a replacement words
  # dictionary, prints out the title and lyrics of the new song
  replacements_dict = {}

  with open(carol_filename) as carol_file:
    with open(replacements) as replacements_file:
      
      
      for replacement_val in replacements_file:        
        (key, value) = replacement_val.split()
        replacements_dict[key] = value     

    for line in carol_file:
      print(convert_line(line, replacements_dict).strip())

 
# Write the rest of your program here
user_original = input("Filename of carol lyrics: ")
user_convert = input("Filename of replacement words: ")

converted = get_replacements(user_convert).get("christmas")

print(f"\nMY {converted.upper()} SONG!")
      

print_new_song(user_original, user_convert)

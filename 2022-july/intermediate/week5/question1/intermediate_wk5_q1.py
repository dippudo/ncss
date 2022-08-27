speech_file = input("Speech file: ")

with open(speech_file, "r") as speech:
  content = speech.read()
  content_list = content.split()
  
  paragraph = []
  
  for word in range(0, 200, 5):
    paragraph.append(content_list[word])
    
print(" ".join(paragraph))

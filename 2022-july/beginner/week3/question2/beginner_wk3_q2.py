length = int(input("Video length? "))

if length < 6:
  print("Too short!")

elif length > 10:
  print("Too long!")

else:
  print("Perfect video length!")

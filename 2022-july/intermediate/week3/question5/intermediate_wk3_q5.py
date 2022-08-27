print("Let's start the walk-a-thon!")

walkList = []
walkLengthTotal = []

walkPerson = " "

while walkPerson:
  walkPerson = input("Who has recorded a walk? ")
  
  if walkPerson != "":
    walkLength = float(input("How far did they walk? "))

    walkLengthTotal.append(walkLength)

    if walkPerson not in walkList:
      walkList.append(walkPerson)
      print(f"That's a first time for {walkPerson}! They walked {walkLength} km!")

    elif walkPerson in walkList:
      print(f"Another walk from {walkPerson}. Well done on another {walkLength} km!")

totalWalkLength = sum(walkLengthTotal)
print(f"Thanks for taking part in the walk-a-thon! We walked a total of {totalWalkLength} km!")

walkList.sort()
print("Here is a list of merit certificate winners:")
for person in walkList:
  print(f"🏅 {person}")

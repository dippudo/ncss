popInitial = int(input("Initial population: "))
popFinal = int(input("Final population: "))

years = 0
popcount = popInitial

while popcount < popFinal:
  popcount = popcount + (0.14 * popcount)
  years = years + 1

print(f"It would take {years} years for there to be {popFinal} cane toads.")

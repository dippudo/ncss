lyric = input("Lyric: ")

lower = lyric.lower()

if "end" not in lower:
  while "end" not in lower:
    print(lyric)
    print("Do doo de do do de doo...")
    
    lyric = input("Lyric: ")
    lower = lyric.lower()

if "end" in lower:
  print("It's the end")

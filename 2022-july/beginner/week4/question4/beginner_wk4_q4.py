two_words = input("Two words? ")

word1 = two_words[0] + two_words[1]
word2 = two_words[-4 : -1] + two_words[-1]

new_word = word1 + word2

print(f"The new word is: {new_word}")

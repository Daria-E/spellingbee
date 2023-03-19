
words = open("./words.txt")
wordList = [word.lower() for word in words.read().splitlines() if word.isalpha()]
centerLetter = input("What is the center letter?").replace(" ", "").lower()
otherLetters = input("What are the other letters?").replace(" ", "").replace(",", "").lower()
allowed = set(centerLetter.lower() + otherLetters.lower())

pangrams = [word for word in wordList if 4 <= len(word) and centerLetter in word and set(word) == allowed]
validWords = [word for word in wordList if 4 <= len(word) and centerLetter in word and set(word) <= allowed]


print("The pangrams are:")
for pangram in pangrams:
    print(pangram)
print()
print("The other words are:")
for word in validWords:
    if word not in pangrams:
        print(word)

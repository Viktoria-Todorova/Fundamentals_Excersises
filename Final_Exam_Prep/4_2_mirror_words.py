import re

text = input()

pattern = r'(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.findall(pattern, text)
pairs_count = 0
mirrored = []
for match in matches:
    word1 = match[1]
    word2 = match[2]

    if word2[::-1] == word1:
        pairs_count += 1

        mirrored.append(f"{word1} <=> {word2}")

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if len(mirrored) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirrored))


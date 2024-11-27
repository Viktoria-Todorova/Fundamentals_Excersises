word = input()
counted_characters = {}

for character in word:
    if character != " ":
        if character not in counted_characters:
            counted_characters[character] = 0

        counted_characters[character] += 1

for key, value in counted_characters.items():
    print(f"{key} -> {value}")

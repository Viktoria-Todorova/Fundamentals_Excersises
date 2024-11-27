
lisy_of_characters = input().split(", ")
list_of_ascii = [ord(character) for character in lisy_of_characters]

merged = dict(zip(lisy_of_characters, list_of_ascii))
print(merged)
characters = int(input())
sum_letters = 0

for letter in range(characters):
    letter_input = input()
    sum_letters += ord(letter_input)

print(f"The sum equals: {sum_letters}")






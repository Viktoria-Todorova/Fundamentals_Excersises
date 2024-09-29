key = int(input())
lines = int(input())

for i in range(lines):
    letter = input()
    letter_numb = ord(letter) + key
    final_letter = chr(letter_numb)
    print(final_letter, end="")

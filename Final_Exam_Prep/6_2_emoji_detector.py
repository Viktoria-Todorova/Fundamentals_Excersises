import re
from operator import index

text = input()
patern_dijit = r"\d"
matched_digits = re.findall(patern_dijit, text)
cool_threshold = 1
for digit in matched_digits:
    cool_threshold *= int(digit)

pattern_emoji = r"(::|\*\*)([A-Z][a-z]{2,})\1"
matched_emoji = re.findall(pattern_emoji, text)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matched_emoji)} emojis found in the text. The cool ones are:")

for emoji in matched_emoji:

    current_emoji = emoji[1]
    ascii_value = 0
    for char in current_emoji:
        ascii_value += ord(char)

    if ascii_value >= cool_threshold:
        print(emoji[0] + current_emoji + emoji[0])


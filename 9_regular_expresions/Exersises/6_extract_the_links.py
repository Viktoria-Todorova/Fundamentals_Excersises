import re

text = input()
pattern = r'[w]{3}\.[A-Za-z0-9\-]+(\.[a-z]+)+'
while text:
    matched = re.search(pattern, text)
    if matched:
        print(matched.group())

    text =input()


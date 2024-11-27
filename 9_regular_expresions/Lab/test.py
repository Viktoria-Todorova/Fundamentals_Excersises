import re

phones = input()
pattern = r'\+359(( |-)(2\1\d{3}\1\d{4}))'

matches = re.findall(pattern, phones)

print(", ".join(matches))
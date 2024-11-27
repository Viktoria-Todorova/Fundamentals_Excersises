import re
from re import match

text = input()

pattern = r'\s((([a-z0-9]+)[a-z0-9\.\-\_]*)@([a-z\-])+(\.[a-z]+)+)\b'


matched = re.findall(pattern, text)

for match in matched:
    print(match[0])

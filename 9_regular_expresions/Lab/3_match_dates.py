import re
dates = input()

pattern = r'\b(\d{2})([-.\/])([A-Z][a-z]{2})([-.\/])(\d{4})'

matches = re.findall(pattern, dates)

for match in matches:
    if match[1] == match[3]:
        print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[4]}")


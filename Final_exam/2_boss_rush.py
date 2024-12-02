import re

inputs = int(input())

for how_many_inputs in range(inputs):
    boss_name_and_title = input()

    pattern = r'^\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#$'

    matches = re.findall(pattern, boss_name_and_title)
    if matches:
        for match in matches:
            print(f"{match[0]}, The {match[1]}")
            print(f">> Strength: {len(match[0])}")
            print(f">> Armor: {len(match[1])}")
    else:
       print("Access denied!")

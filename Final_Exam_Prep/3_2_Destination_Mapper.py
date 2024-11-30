import re

destinations = input()
pattern = r'=[A-Z][A-Za-z]+=|\/[A-Z][A-Za-z]+\/'

valid_destinations = re.findall(pattern, destinations)
destinations = []
travel_points = 0
if valid_destinations:
    for dest in valid_destinations:
        if len(dest[1:-1]) > 2:
            destinations.append(dest[1:-1])
            travel_points += len(dest[1:-1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")



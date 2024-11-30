import re

text = input()
pattern = r'(\||\#)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

matched = re.findall(pattern, text)
total_calories = 0
final_items = []
for match in matched:
    food = match[1]
    date =  match[2]
    calories = int(match[3])
    total_calories += calories
    final_items.append({"food": food, "date": date, "calories": calories})

days = total_calories // 2000


print(f"You have food to last you for: {days} days!")
if final_items:

    for item in final_items:
        print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['calories']}")


import re
brought_furniture = []
total_cost = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'

while True:
    text = input()
    if text == "Purchase":
        break

    matched = re.search(pattern, text)
    if matched:
        furniture,price,quantity = matched.groups()
        brought_furniture.append(furniture)
        total_cost += float(price)*int(quantity)


print("Bought furniture:")
for furniture in brought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
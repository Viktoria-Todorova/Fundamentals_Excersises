items = {'shards': 0,'fragments': 0,'motes': 0}
obtained_item = False

while not obtained_item:
    current_input = input().split()

    for index in range(0,len(current_input),2):
        key = current_input[index + 1].lower()
        value = int(current_input[index])
        if key not in items.keys():
            items[key] = 0
        items[key] += value

        if items["shards"] >= 250:
            print("Shadowmourne obtained!")
            items["shards"] -= 250
            obtained_item = True
        elif items["fragments"] >= 250:
            print("Valanyr obtained!")
            items["fragments"] -= 250
            obtained_item = True
        elif items["motes"] >= 250:
            print("Dragonwrath obtained!")
            items["motes"] -= 250
            obtained_item = True

        if obtained_item:
            break

for key,value in items.items():
    print(f"{key}: {value}")


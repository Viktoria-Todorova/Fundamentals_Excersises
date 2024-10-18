initial_loot = input().split("|")
stolen_loot = []
while True:
    command = input()
    if command == "Yohoho!":
        break
    commands = command.split()
    action = commands[0]

    if action == "Loot":
       for loot in commands[1:]:
           if loot not in initial_loot:
               initial_loot.insert(0, loot)

    elif action == "Drop":
        index = int(commands[1])
        if 0 <= index < len(initial_loot):
            initial_loot.append(initial_loot.pop(index))

    elif action == "Steal":
        count = int(commands[1])
        if count <= len(initial_loot):
            stolen_loot = initial_loot[-count:] # Get the last 'count' elements
            print(", ".join(stolen_loot))
            initial_loot = initial_loot[:-count]
        else:
            stolen_loot = initial_loot[:]
            print(", ".join(stolen_loot))
            initial_loot.clear()



if len(initial_loot) == 0:
    print("Failed treasure hunt.")
elif len(initial_loot) > 0:
    count = 0
    total_sum = 0
    for word in initial_loot:
        count += 1
        total_sum += len(word)

    avg = f"{(total_sum / count):.2f}"

    print(f"Average treasure gain: {avg} pirate credits.")

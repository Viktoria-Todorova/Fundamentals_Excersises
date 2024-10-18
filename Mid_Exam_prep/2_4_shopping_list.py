groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    commant_to = command.split(" ")
    com = commant_to[0]

    if com == "Urgent":
        item = commant_to[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif com == "Unnecessary":
        item = commant_to[1]
        if item in groceries:
            groceries.remove(item)
    elif com == "Correct":
        old_item = commant_to[1]
        new_item = commant_to[2]
        if old_item in groceries:
            ind = groceries.index(old_item)
            groceries[ind] = new_item
    elif com == "Rearrange":
        item = commant_to[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))


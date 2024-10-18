collecting_items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    current_item = command.split(" - ")
    command_for_current_item = current_item[0]

    if command_for_current_item == "Collect":
        item = current_item[1]
        if item not in collecting_items:
            collecting_items.append(item)
    elif command_for_current_item == "Drop":
        item = current_item[1]
        if item in collecting_items:
            collecting_items.remove(item)
    elif command_for_current_item == "Combine Items":
        combined_items = current_item[1].split(":")
        old_item = combined_items[0]
        new_item = combined_items[1]
        if old_item in collecting_items:
            index_of_old_item = collecting_items.index(old_item)
            collecting_items.insert(index_of_old_item + 1, new_item)

    elif command_for_current_item == "Renew":
        item = current_item[1]
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)
print(", ".join(collecting_items))



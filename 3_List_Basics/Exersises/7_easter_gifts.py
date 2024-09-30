names_of_gifts = input().split(" ")

while True:
    commands = input().split(" ")

    if commands[0] == "No" and commands[1] == "Money":
        break
    if commands[0] == "OutOfStock":
        product_name = commands[1]
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i]== product_name:
                names_of_gifts[i] = "None"

    elif commands[0] == "Required":
        product_name = commands[1]
        indexing = int(commands[2])
        if 0 <= indexing < len(names_of_gifts):
            names_of_gifts[indexing] = product_name

    elif commands[0] == "JustInCase":
        product_name = commands[1]
        names_of_gifts[-1] = product_name

final_gift = []
for gift in names_of_gifts:
    if gift != "None":
        final_gift.append(gift)

print(" ".join(final_gift))


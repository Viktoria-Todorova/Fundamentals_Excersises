elements = input().split()
moves = 0
while True:
    command = input()
    if command == "end":
        break
    command_args = command.split()

    ind_1 = int(command_args[0])
    ind_2 = int(command_args[1])
    moves += 1
    if ind_1 == ind_2 or not (0 <= ind_1 < len(elements)) or not (0 <= ind_2 < len(elements)):
        middle_index = len(elements) // 2
        elements.insert(middle_index, f"-{moves}a")
        elements.insert(middle_index, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    else:
        if elements[ind_1] == elements[ind_2]:
            element = elements[ind_1]
            print(f"Congrats! You have found matching elements - {element}!")
            elements.pop(max(ind_1,ind_2))
            elements.pop(min(ind_1,ind_2))
        else:
            print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))

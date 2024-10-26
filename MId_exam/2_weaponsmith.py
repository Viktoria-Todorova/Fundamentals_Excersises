name_of_weapon = input().split("|")
while True:
    command = input()
    if command == "Done":
        print(f"You crafted {''.join(name_of_weapon)}!")
        break
    current_command = command.split(" ")
    supported_command = current_command[0]
    if supported_command == "Add":
        particle = current_command[1]
        index = int(current_command[2])

        if 0 <= index < len(name_of_weapon):
            name_of_weapon.insert(index, particle)

    elif supported_command == "Remove":
        index = int(current_command[1])

        if 0 <= index < len(name_of_weapon):
            name_of_weapon.pop(index)

    elif supported_command == "Check":

        if current_command[1] == "Even":
            even_nums = []
            for ind in name_of_weapon:
                index = name_of_weapon.index(ind)
                if index % 2 == 0:
                    even_nums.append(ind)
            print(*even_nums)
        elif current_command[1] == "Odd":
            odd_nums = []
            for ind in name_of_weapon:
                index = name_of_weapon.index(ind)
                if index % 2 != 0:
                    odd_nums.append(ind)
            print(*odd_nums)





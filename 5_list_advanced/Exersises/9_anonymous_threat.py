characters = input().split()

while True:
    command = input()

    if command == "3:1":
        break
    splited_command = command.split()
    action = splited_command[0]

    if action == "merge":
        start_index = int(splited_command[1])
        end_index = int(splited_command[2])
        start_index = max(0, start_index)
        end_index = min(len(characters) - 1, end_index)

        merging = "".join(characters[start_index:end_index+1])
        characters = characters[:start_index] + [merging] + characters[end_index + 1:]


    elif action == "divide":
        ind = int(splited_command[1])
        partitions = int(splited_command[2])

        element_to_divide = characters[ind]

        partion_size = len(element_to_divide) // partitions
        remainder = len(element_to_divide) % partitions

        new_substring = []
        start_ind = 0

        for i in range(partitions):
            size =start_ind + partion_size + (1 if i < remainder else 0)
            new_substring.append(element_to_divide[start_ind:size])
            start_ind = size
        characters = characters[:ind] + new_substring + characters[ind + 1:]



print(" ".join(characters))

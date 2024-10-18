array = list(map(int, input().split()))
new_list = []
while True:
    command = input()
    if command == "end":
        break
    elements = command.split()
    command_type = elements[0]
    if command_type == "swap":
        index_1 = int(elements[1])
        index_2 = int(elements[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]

    elif command_type == "multiply":
        index_1 = int(elements[1])
        index_2 = int(elements[2])
        array[index_1] = int(array[index_1]) * int(array[index_2])

    elif command_type == "decrease":
        for index in range(len(array)):
            array[index] -= 1

print(", ".join(map(str, array)))

seq_of_target = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    command_elements = command.split()
    command_for_manipulation = command_elements[0]
#Shoot the target at the index if it exists by reducing
# its value by the given power (integer value).
    if command_for_manipulation == "Shoot":
        index = int(command_elements[1])
        power = int(command_elements[2])
        if 0 <= index < len(seq_of_target):
            seq_of_target[index] -= power
            #Remove the target if it is shot.
            # A target is considered shot when its value reaches 0
            if seq_of_target[index] <= 0:
                seq_of_target.pop(index)

#Insert a target with the received value at the received index if it exists.
    elif command_for_manipulation == "Add":
        index = int(command_elements[1])
        value = command_elements[2]
        if 0 <= index < len(seq_of_target):
            seq_of_target.insert(index, int(value))
        else:
            print("Invalid placement!")

    elif command_for_manipulation == "Strike":
        index = int(command_elements[1])
        radius = int(command_elements[2])

        if index - radius >= 0 and index + radius < len(seq_of_target):
            del seq_of_target[index - radius:index + radius + 1]
        else:
            print("Strike missed!")
            continue

print("|".join(map(str,seq_of_target)))

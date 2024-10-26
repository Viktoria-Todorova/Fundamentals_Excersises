wagons = int(input())
train = [0] * wagons # Create a list with the specified length containing only zeros
while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    command_type = command[0]
    if command_type == "add":
        people = int(command[1])
        train[-1] += people
    elif command_type == "insert":
        index = int(command[1])
        people = int(command[2])
        train[index] += people
    elif command_type == "leave":
        index = int(command[1])
        people = int(command[2])
        train[index] -= people

print(train)



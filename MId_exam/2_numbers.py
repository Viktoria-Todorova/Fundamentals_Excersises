numbers = input().split()

while True:
    command = input()
    if command == "Finish":
        break
    commands = command.split()
    action = commands[0]
    if action == "Add":
        value = commands[1]
        numbers.append(value)
    elif action == "Remove":
        value = commands[1]
        if str(value)in numbers:
            numbers.remove(value)
    elif action == "Replace":
        value1 = commands[1]
        replacment = commands[2]
        if value1 in numbers:
            numbers[numbers.index(value1)] = replacment
    elif action == "Collapse":
        value = int(commands[1])
        keep = [num for num in numbers if int(num) >= value]
        numbers = keep
print(" ".join(map(str, numbers)))
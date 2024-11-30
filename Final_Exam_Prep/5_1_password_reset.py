text = input()

while True:
    command = input()
    if command == 'Done':
        break
    splitted_command = command.split()
    action = splitted_command[0]

    if action == 'TakeOdd':
        new_text = ""
        for ind in range(len(text)):
            if ind % 2 != 0:
                new_text += text[ind]
        text = new_text
        print(text)

    elif action == "Cut":
        index = int(splitted_command[1])
        length = int(splitted_command[2])
        substring = text[index:index+length]
        text = text.replace(substring, '',1)
        print(text)

    elif action == "Substitute":
        substring = splitted_command[1]
        substitude = splitted_command[2]
        if substring in text:
            text = text.replace(substring, substitude)
            print(text)
        else:
            print("Nothing to replace!")
print(f"Your password is: {text}")
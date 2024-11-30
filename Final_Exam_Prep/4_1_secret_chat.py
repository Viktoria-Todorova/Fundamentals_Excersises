concealed_message = input()

command = input()
while command != 'Reveal':
    instructions = command.split(":|:")
    current_instruction = instructions[0]

    if current_instruction == 'InsertSpace':
        index = int(instructions[1])
        concealed_message = concealed_message[:index] + " "+  concealed_message[index:]
        print(concealed_message)
    elif current_instruction == 'Reverse':
        sunsting = instructions[1]
        if sunsting in concealed_message:
            #This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
            concealed_message = concealed_message.replace(sunsting, "",1)
            reverse_message = sunsting[::-1]
            concealed_message += reverse_message
            print(concealed_message)
        else:
            print("error")
    elif current_instruction == 'ChangeAll':
        substring = instructions[1]
        replacement = instructions[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)


    command = input()
print(f"You have a new text message: {concealed_message}")
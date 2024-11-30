activation_key = input()

while True:
    command = input()

    if command == 'Generate':
        break

    split_command = command.split('>>>')
    instruction = split_command[0]
    if instruction == 'Contains':
        substring = split_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif instruction == 'Flip':
        upper_or_lower = split_command[1]
        start_index = int(split_command[2])
        end_index = int(split_command[3])
        substring = activation_key[start_index:end_index]
        if upper_or_lower == 'Upper':

            activation_key = activation_key[:start_index] + substring.upper() + activation_key[end_index:]

        elif upper_or_lower == 'Lower':
           activation_key = activation_key[:start_index] + substring.lower() + activation_key[end_index:]

        print(activation_key)
    elif instruction == 'Slice':
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

print(f"Your activation key is: {activation_key}")
encrypted_message = input()

while True:
    command = input()
    if command == 'Decode':
        print(f"The decrypted message is: {encrypted_message}")
        break
    splitted_message = command.split("|")
    action = splitted_message[0]

    if action == "Move":
        num_of_letters = int(splitted_message[1])
        first_letter = encrypted_message[num_of_letters:]
        second_letter = encrypted_message[:num_of_letters]
        encrypted_message = first_letter + second_letter

    elif action == "Insert":
        index = int(splitted_message[1])
        value = splitted_message[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]


    elif action == "ChangeAll":
        substring = splitted_message[1]
        replacement = splitted_message[2]
        encrypted_message=encrypted_message.replace(substring, replacement)





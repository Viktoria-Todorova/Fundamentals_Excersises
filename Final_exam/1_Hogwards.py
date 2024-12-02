spell = input()

while True:
    command = input()
    if command == "Abracadabra":
        break

    command_to_split = command.split()
    action = command_to_split[0]

    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index = int(command_to_split[1])
        letter = command_to_split[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index + 1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        firs_substring = command_to_split[1]
        second_substring = command_to_split[2]
        if firs_substring in spell:
            spell = spell.replace(firs_substring, second_substring)
            print(spell)

    elif action == "Alteration":
        substring = command_to_split[1]
        if substring in spell:
            spell = spell.replace(substring,"")
            print(spell)

    else:
        print("The spell did not work!")

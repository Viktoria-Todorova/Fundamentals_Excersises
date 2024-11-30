number_of_pieces = int(input())
pieces_dictionary = {}

for piece in range(number_of_pieces):
    splited_pieces = input().split("|")
    pieces = splited_pieces[0]
    composer = splited_pieces[1]
    key = splited_pieces[2]

    if pieces not in pieces_dictionary:
        pieces_dictionary[pieces] = [composer,key]

while True:
    command = input()
    if command == "Stop":

        break
    splitted_command = command.split("|")
    action = splitted_command[0]
    piece = splitted_command[1]

    if action == "Add":
        current_composer = splitted_command[2]
        key = splitted_command[3]
        if piece not in pieces_dictionary:
            pieces_dictionary[piece] = [current_composer,key]
            print(f"{piece} by {current_composer} in {key} added to the collection!" )
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        if piece in pieces_dictionary:
            del pieces_dictionary[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


    elif action == "ChangeKey":
        new_key = splitted_command[2]

        if piece in pieces_dictionary:
            pieces_dictionary[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in pieces_dictionary.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")



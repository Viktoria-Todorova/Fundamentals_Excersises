list_of_songs = input().split()
count_commands = int(input())

for command in range(count_commands):
    current_command = input().split(" * ")

    action = current_command[0]

    if action == "Add Song":
        song = current_command[1]
        if song not in list_of_songs:
            list_of_songs.append(song)
            print(f"{song} successfully added")

    elif action == "Delete Song":
        number_song = int(current_command[1])
        if number_song in range(len(list_of_songs)):
            removed_songs = list_of_songs[:number_song ]
            print(f"{', '.join(removed_songs)} deleted")
            list_of_songs = list_of_songs[number_song:]


    elif action == "Shuffle Songs":
        song_ind_1 = int(current_command[1])
        song_ind_2 = int(current_command[2])
        if song_ind_1 in range(len(list_of_songs)) and song_ind_2 in range(len(list_of_songs)):
            list_of_songs[song_ind_1], list_of_songs[song_ind_2] = list_of_songs[song_ind_2], list_of_songs[song_ind_1]
            print(f"{list_of_songs[song_ind_2]} is swapped with {list_of_songs[song_ind_1]}")
    elif action == "Insert":
        song = current_command[1]
        index = int(current_command[2])
        if index in range(len(list_of_songs)):
            if song not in list_of_songs:
                list_of_songs.insert(index, song)
                print(f"{song} successfully inserted")
            else:
                print("Song is already in the playlist")

        else:
            print("Index out of range")
    elif action == "Sort":
        list_of_songs.sort(reverse=True)

    elif action == "Play":
        print(f"Songs to Play:")
        for songs in list_of_songs:
            print(songs)





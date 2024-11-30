
stops = input()

command = input()

while True:

    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {stops}")
        break
    splitted_command = command.split(":")
    manipulation= splitted_command[0]

    if manipulation == "Add Stop":
        index = int(splitted_command[1])
        current_string = splitted_command[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + current_string + stops[index:]
            print(stops)
        else:
            print(stops)

    elif manipulation == "Remove Stop":
        star_index = int(splitted_command[1])
        end_index = int(splitted_command[2])
        if 0 <= star_index <= end_index < len(stops):
            stops = stops[:star_index] + stops[end_index+1:]
            print(stops)
        else:
            print(stops)


    elif manipulation == "Switch":
        old_sting = splitted_command[1]
        new_string = splitted_command[2]
        if old_sting in stops:
            stops = stops.replace(old_sting,new_string)
            print(stops)
        else:
            print(stops)
    command =input()

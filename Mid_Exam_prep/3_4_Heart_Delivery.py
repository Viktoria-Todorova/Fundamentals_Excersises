neighborhood = list(map(int, input().split("@")))

last_position = 0
working_index = 0
while True:
    command = input()
    if command == "Love!":
        break
    jump_command = command.split()

    jump_lenght = int(jump_command[1])
    current_index = working_index + jump_lenght

    if 0 <= current_index < len(neighborhood):
        working_index = current_index

    else:
        working_index = 0

    hearts = neighborhood[working_index]

    if hearts == 0:
        print(f"Place {working_index} already had Valentine's day.")

    else:
        neighborhood[working_index] -= 2
        if neighborhood[working_index] == 0:
            print(f"Place {working_index} has Valentine's day." )

    last_position = working_index

print(f"Cupid's last position was {last_position}.")

failed_houses = len([failed for failed in neighborhood if failed > 0])

if failed_houses > 0:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")





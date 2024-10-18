pirat_ship_section = [int(section) for section in input().split(">")]
war_ship_section = [int(section) for section in input().split(">")]
max_helth = int(input())
pirat_ship_sunk = False
war_ship_sunk = False
while True:
    command = input()
    if command == "Retire":
        break

    command_elements = command.split()
    command_for_manipulation = command_elements[0]

    if command_for_manipulation == "Fire":
        index = int(command_elements[1])
        damage = int(command_elements[2])
        if 0 <= index < len(war_ship_section):
            war_ship_section[index] -= damage
            if war_ship_section[index] <= 0:

                war_ship_sunk = True
                break



    elif command_for_manipulation == "Defend":
        start_index = int(command_elements[1])
        end_index = int(command_elements[2])
        damage = int(command_elements[3])
        if start_index in range(len(pirat_ship_section)) and end_index in range(len(pirat_ship_section)):
            for attack in range(start_index, end_index + 1):
                pirat_ship_section[attack] -= damage
                if pirat_ship_section[attack] <= 0:
                    pirat_ship_sunk = True
                    break

    elif command_for_manipulation == "Repair":
        index = int(command_elements[1])
        health = int(command_elements[2])
        if 0 <= index < len(pirat_ship_section):
            pirat_ship_section[index] += health
            if pirat_ship_section[index] > max_helth:
                pirat_ship_section[index] = max_helth

    elif command_for_manipulation == "Status":
        count_section_for_repair = 0
        for stats in range(len(pirat_ship_section)):
            if pirat_ship_section[stats] < (max_helth * 0.2):
                count_section_for_repair += 1
        print(f"{count_section_for_repair} sections need repair.")
if war_ship_sunk:
    print("You won! The enemy ship has sunken.")
elif pirat_ship_sunk:
    print("You lost! The pirate ship has sunken.")
else:
    print(f"Pirate ship status: {sum(pirat_ship_section)}")
    print(f"Warship status: {sum(war_ship_section)}")



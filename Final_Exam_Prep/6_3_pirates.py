caribian_dictionary = {}
while True:
    command = input()
    if command == 'Sail':
        break
    command_to_split = command.split("||")
    cities = command_to_split[0]
    population = int(command_to_split[1])
    gold = int(command_to_split[2])
    if cities not in caribian_dictionary:
        caribian_dictionary[cities] = [population, gold]
    else:
        caribian_dictionary[cities][0] += population
        caribian_dictionary[cities][1] += gold

while True:
    command = input()
    if command == 'End':
        break
    command_to_split = command.split("=>")
    action = command_to_split[0]
    town = command_to_split[1]


    if action == 'Plunder':
        people = int(command_to_split[2])
        gold = int(command_to_split[3])
        caribian_dictionary[town][0]-= people
        caribian_dictionary[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if caribian_dictionary[town][0] <= 0 or caribian_dictionary[town][1] <= 0:
            del caribian_dictionary[town]
            print(f"{town} has been wiped off the map!")

    elif action == 'Prosper':
        gold = int(command_to_split[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            caribian_dictionary[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {caribian_dictionary[town][1]} gold.")



if caribian_dictionary:
    print(f"Ahoy, Captain! There are {len(caribian_dictionary)} wealthy settlements to go to:")
    for key, value in caribian_dictionary.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
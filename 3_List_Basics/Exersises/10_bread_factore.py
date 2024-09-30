working_day_event = input().split("|")

initial_energy = 100
initial_coins = 100
count_events = 0
for event in working_day_event:
    working_day = event.split("-")
    current_event = working_day[0]
    current_ingredient = working_day[1]
    current_ingredient_to_int = int(current_ingredient)

    if current_event == "rest":
        count_events += 1
        energy_gained = min(100 - initial_energy, current_ingredient_to_int)
        initial_energy += energy_gained
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {initial_energy}.")


    elif current_event == "order":
        count_events += 1

        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += current_ingredient_to_int
            print(f"You earned {current_ingredient_to_int} coins.")
        else:
            print("You had to rest!")
            initial_energy += 50

    else:
        count_events += 1
        if initial_coins >= current_ingredient_to_int:
            initial_coins -= current_ingredient_to_int
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            break


else:
    print(f"Day completed!\n"
            f"Coins: {initial_coins}\n"
            f"Energy: {initial_energy}\n"
            )



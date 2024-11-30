
number_of_heroes = int(input())
hero_dictionary = {}
for _ in range(number_of_heroes):
    hero = input().split()
    hero_name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])
    if hp <= 100 and mp <= 200:
        hero_dictionary[hero_name] = [hp,mp]


while True:
    command = input()

    if command == 'End':
        break

    splitted_command = command.split(" - ")

    action = splitted_command[0]
    current_hero_name = splitted_command[1]

    if action == 'CastSpell':
        mp_needed = int(splitted_command[2])
        spell_name = splitted_command[3]
        if int(hero_dictionary[current_hero_name][1]) >= mp_needed:
            hero_dictionary[current_hero_name][1] -= mp_needed
            print(f"{current_hero_name} has successfully cast {spell_name} and now has {hero_dictionary[current_hero_name][1]} MP!")
        else:
            print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(splitted_command[2])
        attacker = splitted_command[3]
        hero_dictionary[current_hero_name][0] -= damage
        if hero_dictionary[current_hero_name][0] > 0:
            print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {hero_dictionary[current_hero_name][0]} HP left!")
        else:
            print(f"{current_hero_name} has been killed by {attacker}!")
            del hero_dictionary[current_hero_name]

    elif action == 'Recharge':
        amount = int(splitted_command[2])
        if int(hero_dictionary[current_hero_name][1]) + amount <200:
            hero_dictionary[current_hero_name][1] += amount
            print(f"{current_hero_name} recharged for {amount} MP!")
        else:
            extra = 200 - int(hero_dictionary[current_hero_name][1])
            hero_dictionary[current_hero_name][1] = 200
            print(f"{current_hero_name} recharged for {extra} MP!")


    elif action == 'Heal':
        amount = int(splitted_command[2])
        if int(hero_dictionary[current_hero_name][0]) + amount <100:
            hero_dictionary[current_hero_name][0] += amount
            print(f"{current_hero_name} healed for {amount} HP!")
        else:
            extra = 100 - int(hero_dictionary[current_hero_name][0])
            hero_dictionary[current_hero_name][0] = 100
            print(f"{current_hero_name} healed for {extra} HP!")

if hero_dictionary:
    for key, value in hero_dictionary.items():
        print(f"{key}\nHP: {value[0]}\nMP: {value[1]} ")
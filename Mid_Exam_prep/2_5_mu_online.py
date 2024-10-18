dungeons_room = input().split("|")
health = 100
bitcoin = 0
room_count = 0

for room in dungeons_room:
    room_count += 1
    room_info = room.split(" ")
    command = room_info[0]
    if command == "potion":
        difference = 0
        amount = int(room_info[1])
        if health + amount >= 100:
            difference = 100 - health
            health = 100

        else:
            health += amount
            difference = amount

        print(f"You healed for {difference} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoin += int(room_info[1])
        print(f"You found {room_info[1]} bitcoins.")
    else:
        damage = int(room_info[1])
        health -= damage
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
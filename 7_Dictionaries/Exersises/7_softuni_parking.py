number_of_commands = int(input())
dictionary_of_cars = {}
for i in range(number_of_commands):
    command = input().split()

    if "register" in command:
        username = command[1]
        license_plate = command[2]
        if username in dictionary_of_cars:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            dictionary_of_cars[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif "unregister" in command:
        username = command[1]
        if username not in dictionary_of_cars:
            print(f"ERROR: user {username} not found")
        else:
            del dictionary_of_cars[username]
            print(f"{username} unregistered successfully")

for key, value in dictionary_of_cars.items():
    print(f"{key} => {value}")
count_coffee = 0
while True:
    commands = input()

    if commands == "END":
        break
    else:
        lower_command = commands.lower()
        if lower_command in ["coding", "cat", "dog", "movie"]:
            if commands.islower():
                count_coffee += 1
            elif commands.isupper():
                count_coffee += 2

if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)



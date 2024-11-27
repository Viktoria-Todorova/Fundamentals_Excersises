current_dictionary = {}
course_points = {}
while True:
    command = input()

    if command == 'exam finished':
        break

    if "banned" in command:
        splitted_txt = command.split("-")
        username = splitted_txt[0]
        del current_dictionary[username]
        continue

    splitted_command = command.split('-')
    username = splitted_command[0]
    language = splitted_command[1]
    points = int(splitted_command[2])

    if username not in current_dictionary:
        current_dictionary[username] = 0

    if points > current_dictionary[username]:
        current_dictionary[username] = points

    if language not in course_points.keys():
        course_points[language] = 0
    course_points[language] += 1

print("Results:")
for username, points in current_dictionary.items():

    print(f"{username} | {points}")
print("Submissions:")
for course, points in course_points.items():
    print(f"{course} - {points}")



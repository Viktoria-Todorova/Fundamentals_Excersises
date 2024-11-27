dicti_of_resourses = {}
while True:
    command = input()

    if command == 'stop':
        break

    resource = command
    quantity = int(input())
    if resource not in dicti_of_resourses:
        dicti_of_resourses[resource] = 0
    dicti_of_resourses[resource] += quantity

for key, value in dicti_of_resourses.items():
    print(f'{key} -> {value}')




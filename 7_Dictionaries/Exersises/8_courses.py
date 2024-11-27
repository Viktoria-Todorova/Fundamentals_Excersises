programs = {}
while True:
    command = input()

    if command == 'end':
        break
    com = command.split(" : ")

    course_name = com[0]
    student_name = com[1]

    if course_name not in programs:
        programs[course_name] = []
    programs[course_name].append(student_name)

for key, value in programs.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")



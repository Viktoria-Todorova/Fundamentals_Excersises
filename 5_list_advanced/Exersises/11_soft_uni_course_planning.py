initial_schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    new_command = command.split(":")
    command_for_course = new_command[0]

    if command_for_course == "Add":
        lesson_title = new_command[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)

    elif command_for_course == "Insert":
        lesson_title = new_command[1]
        index = int(new_command[2])
        if lesson_title not in initial_schedule:
            if 0 <= index <= len(initial_schedule): #check if index is valid
                initial_schedule.insert(index, lesson_title)

    elif command_for_course == "Remove":
        lesson_title = new_command[1]
        if lesson_title in initial_schedule:
            if f"{lesson_title}-Exercise" in initial_schedule:
                initial_schedule.remove(f"{lesson_title}-Exercise")
            initial_schedule.remove(lesson_title)

    elif command_for_course == "Swap":
        lesson_title = new_command[1]
        swap_with = new_command[2]
        if lesson_title in initial_schedule and swap_with in initial_schedule:
            index_lesson_title = initial_schedule.index(lesson_title)
            index_swap_with = initial_schedule.index(swap_with)
            initial_schedule[index_lesson_title], initial_schedule[index_swap_with] = \
                initial_schedule[index_swap_with], initial_schedule[index_lesson_title]

            lesson_exercise = f"{lesson_title}-Exercise"
            swap_with_exercise = f"{swap_with}-Exercise"

            if lesson_exercise in initial_schedule and swap_with_exercise in initial_schedule:
                # Find their indices and swap them
                exercise_index1 = initial_schedule.index(lesson_exercise)
                exercise_index2 = initial_schedule.index(swap_with_exercise)
                initial_schedule[exercise_index1], initial_schedule[exercise_index2] = \
                    initial_schedule[exercise_index2], initial_schedule[exercise_index1]
            else:
                if lesson_exercise in initial_schedule:
                    # Remove the exercise from its original position
                    initial_schedule.remove(lesson_exercise)
                    # Insert it right after the swapped lesson
                    new_index_lesson = initial_schedule.index(lesson_title)
                    initial_schedule.insert(new_index_lesson + 1, lesson_exercise)

                if swap_with_exercise in initial_schedule:
                    # Remove the exercise from its original position
                    initial_schedule.remove(swap_with_exercise)
                    # Insert it right after the swapped lesson
                    new_index_swap_with = initial_schedule.index(swap_with)
                    initial_schedule.insert(new_index_swap_with + 1, swap_with_exercise)


    elif command_for_course == "Exercise":
        lesson_title = new_command[1]
        if lesson_title not in initial_schedule:
            initial_schedule.append(lesson_title)
            initial_schedule.append(f"{lesson_title}-Exercise")
        else:
            if f"{lesson_title}-Exercise" not in initial_schedule:
                lesson_index = initial_schedule.index(lesson_title)
                initial_schedule.insert(lesson_index + 1, f"{lesson_title}-Exercise")


for index,lesson in enumerate(initial_schedule):
    print(f"{index +1}.{lesson}")


students =int(input())
lectures = int(input())
additional_bonus = int(input())
max_lecture = 0

max_num = 0
for student in range(students):
    attendance = int(input())
    if lectures >0:
        bonus = (attendance / lectures) * (5 + additional_bonus)
    else:
        bonus = 0
    if bonus > max_num:
        max_num = bonus
        max_lecture = attendance


print(f"Max Bonus: {round(max_num)}.")
print(f"The student has attended {max_lecture} lectures.")


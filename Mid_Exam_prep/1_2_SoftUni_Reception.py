empl_1 = int(input())
empl_2 = int(input())
empl_3 = int(input())
students_count = int(input())

total_count_stud = empl_1 + empl_2 + empl_3
count_hours = 0
while students_count > 0:
    count_hours += 1
    if count_hours % 4 == 0:
        count_hours +=1
    if students_count >= total_count_stud:
        students_count -=total_count_stud
    else:
        students_count = 0
        break
print(f"Time needed: {count_hours}h.")




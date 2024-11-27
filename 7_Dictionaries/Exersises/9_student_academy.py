rows = int(input())
students = {}
for row in range(rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = {
            "grade" : 0,
            "count_grades": 0
               }

    students[student_name]["grade"] += student_grade
    students[student_name]["count_grades"] += 1

for key, value in students.items():
    average_grade = value["grade"] / value["count_grades"]
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")
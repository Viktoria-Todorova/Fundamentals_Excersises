employees_happines = input().split()
factor = int(input())
employees = list(map(lambda x: int(x)*factor, employees_happines))
avg_happines = sum(employees)/len(employees)
filter_happiness = list(filter(lambda x: x >= avg_happines, employees))

if len(filter_happiness) < len(employees)/2:
    print(f"Score: {len(filter_happiness)}/{len(employees)}. Employees are not happy!")
else:
    print(f"Score: {len(filter_happiness)}/{len(employees)}. Employees are happy!")
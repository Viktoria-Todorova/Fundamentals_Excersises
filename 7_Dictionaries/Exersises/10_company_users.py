employees_info = {}

while True:
    info = input()

    if info == "End":
        break
    company_info = info.split(" -> ")
    company_name = company_info[0]
    employee_id = company_info[1]

    if company_name not in employees_info:
        employees_info[company_name] = []
    if employee_id not in employees_info[company_name]:
        employees_info[company_name].append(employee_id)
for key, value in employees_info.items():
    print(f"{key}")
    for employee in value:
        print(f"-- {employee}")



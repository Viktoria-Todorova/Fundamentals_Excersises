import math

from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_eggs = float(input())
price_apron =float(input())

free_pacages = students // 5

flour_for_students = (students - free_pacages) * price_flour
eggs_for_students = students * price_eggs * 10
apron_for_students = ceil(students * 1.20) * price_apron


total_price = flour_for_students + eggs_for_students + apron_for_students

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price-budget:.2f}$ more needed.")

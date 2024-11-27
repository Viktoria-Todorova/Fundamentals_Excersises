import re
numbers = input()


pattern= r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

valid_number = re.findall(pattern, numbers)
for num in range(len(valid_number)):
    if num < len(valid_number) - 1:
        print(valid_number[num], end=', ')
    else:
        print(valid_number[num])
from sys import maxsize
max_num = -maxsize
number_snowballs = int(input())
current_weight = 0
current_time = 0
current_quality = 0

for data in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (weight/time) ** quality
    if snowball_value > max_num:
        max_num =snowball_value
        current_weight = weight
        current_time = time
        current_quality = quality

print(f"{current_weight} : {current_time} = {max_num:.0f} ({current_quality})")




numbers = input().split()
total_time_first = 0
total_time_second = 0

middle_index = len(numbers)//2

left_racer = numbers[:middle_index ]
right_racer = numbers[middle_index+1:][::-1]

for time in left_racer:
    if int(time) == 0:
        total_time_first -= total_time_first * 0.2
    else:
        total_time_first += int(time)

for time2 in right_racer:
    if int(time2) == 0:
        total_time_second -= total_time_second * 0.2
    else:
        total_time_second += int(time2)

if total_time_first < total_time_second:
    print(f"The winner is left with total time: {total_time_first:.1f}")
else:
    print(f"The winner is right with total time: {total_time_second:.1f}")

numbers = input().split(", ")
new_list = []
for ind in range(len(numbers)):
    num = int(numbers[ind])
    current_index = ind
    if num % 2 == 0:
        new_list.append(current_index)

print(new_list)
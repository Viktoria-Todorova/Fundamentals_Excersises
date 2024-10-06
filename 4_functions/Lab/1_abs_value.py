sequence_of_nums = input().split()
final_list =[]

for num in sequence_of_nums:
    absolute_value = abs(float(num))
    final_list.append(absolute_value)
print(final_list)

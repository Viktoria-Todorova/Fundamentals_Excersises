from audioop import reverse

list_of_nums=list(map(int, input().split()))
total_sum = 0
total_times = 0
final_list = []
for num in list_of_nums:
    total_sum += int(num)
    total_times += 1

average_value = total_sum // total_times

final_list = sorted([num for num in list_of_nums if int(num) > average_value], reverse=True)
if 0 < len(final_list) < 5:
    print(" ".join(map(str, final_list)))
elif len(final_list) == 0:
    print("No")
else:
    print(" ".join(map(str,final_list[:5])))




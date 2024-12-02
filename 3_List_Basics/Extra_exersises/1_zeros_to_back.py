numbers = input().split(',')
list_with_num = []
list_with_none = []

for number in numbers:
    number_int = int(number)

    if number_int == 0:
        list_with_none.append(number_int)
    else:
        list_with_num.append(number_int)
final_list = list_with_num + list_with_none

print(final_list)

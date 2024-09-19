number = int(input())
number_to_string = str(number)

sorted_num = sorted(number_to_string, reverse=True)

int_numbers = int(''.join(sorted_num))

print(int_numbers)

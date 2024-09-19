from sys import maxsize

max_num = -maxsize

number = int(input())
number_to_string = str(number)
final_num = ''
for digit in number_to_string:

    digit_to_num = int(digit)

    if digit_to_num > max_num:
        max_num = digit_to_num
        final_num = digit

print(final_num, end="")

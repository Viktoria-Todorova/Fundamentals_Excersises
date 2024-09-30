string_input = input()
str_to_num = string_input.split()

opposite = [-int(num) for num in str_to_num]

print(opposite)

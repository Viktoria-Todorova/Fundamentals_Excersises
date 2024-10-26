version = input().split(".")
num_list = ""
for num in version:
    number = str(num)
    num_list += number

num_to_int= int(num_list)
next_num = num_to_int + 1
next_num_to_str = str(next_num)
print(".".join(next_num_to_str))





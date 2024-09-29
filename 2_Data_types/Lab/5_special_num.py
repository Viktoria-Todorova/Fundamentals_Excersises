number = int(input())

for i in range(1,number+1):
    sum_digits = sum(int(digit) for digit in str(i))

    special_num = [5,7,11]
    special = sum_digits in special_num

    print(f"{i} -> {special}")



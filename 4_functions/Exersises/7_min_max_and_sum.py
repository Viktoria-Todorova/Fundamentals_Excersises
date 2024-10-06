def min_max_and_sum(num):
    int_nums = []
    for n in num:
        int_nums.append(int(n))

    minimum = min(int_nums)
    maximum = max(int_nums)
    sum_nums = sum(int_nums)
    return f"The minimum number is {minimum}\nThe maximum number is {maximum}\nThe sum number is: {sum_nums}"
numbers = input().split()
print(min_max_and_sum(numbers))

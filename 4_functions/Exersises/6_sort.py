
def num_sorted (number):
    num_to_sort = []
    for num in number:
        str_to_int = int(num)
        num_to_sort.append(str_to_int)
    return sorted(num_to_sort)


nums = input().split()
print([int(numbers) for numbers in num_sorted(nums)])
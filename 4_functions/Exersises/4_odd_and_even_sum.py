
def odd_even_sum(num):
    sum_even = 0
    sum_odd = 0
    for numb in num:

        if int(numb) % 2 == 0:
            sum_even += int(numb)
        else:
            sum_odd += int(numb)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

number = input()
print(odd_even_sum(number))
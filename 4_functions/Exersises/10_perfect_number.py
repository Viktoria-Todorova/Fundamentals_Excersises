def perfect_num(num):
    division_sum = 0
    for numb in range(1,num):
        if num % numb == 0:
            division_sum += numb
    if division_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number =int(input())
print( perfect_num(number))
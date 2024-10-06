def factorial_dividsion(num1,num2):
    fact_1 = 1
    fact_2 = 1
    for first in range(2,num1+1):
        fact_1 *= first
    for second in range(2,num2+1):
        fact_2 *= second

    result = fact_1 / fact_2
    return f"{result:.2f}"

numb_1 = int(input())
numb_2 = int(input())
print(factorial_dividsion(numb_1,numb_2))

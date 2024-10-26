def multiplication_sign(a,b,c):

    if a == 0 or b == 0 or c == 0:
        return "zero"
    negatives = 0
    if a < 0:
        negatives += 1
    if b < 0:
        negatives += 1
    if c < 0:
        negatives += 1

    # If there are an odd number of negative numbers, the product is negative
    if negatives % 2 == 1:
        return "negative"
    else:
        return "positive"

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(multiplication_sign(num1,num2,num3))
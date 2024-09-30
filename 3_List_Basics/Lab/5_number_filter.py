num = int(input())
even_num = []
odd_num = []
negative_num = []
positive_num = []


for tests in range(num):
    n_int = int(input())

    if n_int < 0:
        negative_num.append(n_int)
    if n_int >= 0:
        positive_num.append(n_int)
    if n_int %2 == 0:
        even_num.append(n_int)
    elif n_int % 2 != 0:
        odd_num.append(n_int)

command = input()

if command == "even":
    print(even_num)
elif command == "odd":
    print(odd_num)
elif command == "negative":
    print(negative_num)
elif command == "positive":
    print(positive_num)


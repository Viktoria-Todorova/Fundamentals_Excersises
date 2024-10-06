parameter = input()
num_1 = int(input())
num_2 = int(input())

def solve():

    if parameter == "multiply":
        return num_1 * num_2
    elif parameter == "divide":
        return int(num_1 / num_2)
    elif parameter == "add":
        return num_1 + num_2
    elif parameter == "subtract":
        return num_1 - num_2

print(solve())
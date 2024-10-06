numbers = input().split(" ")

def round_nums():
    list_of_rounded = []
    for num in numbers:
        str_to_int = round(float(num))
        list_of_rounded.append(str_to_int)
    return list_of_rounded

print(round_nums())





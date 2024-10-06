def loading_bar(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    count_percent = num // 10
    count_dots = 10 - count_percent
    return f"{num}% [{'%' * count_percent}{'.' * count_dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))
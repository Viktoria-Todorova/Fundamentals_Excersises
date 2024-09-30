
money_given = input().split(", ")
beggars = int(input())

money_as_int = []
money_beggar = 0

for money in money_given:
    money_as_int.append(int(money))

list_with_beggars = []
index = 0

for current_beggar in range(beggars):
    current_beggar_sum = 0

    for current_money in range(index, len(money_as_int),beggars):
        current_beggar_sum += money_as_int[current_money]

    list_with_beggars.append(current_beggar_sum)
    index += 1


print(list_with_beggars)


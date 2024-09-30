cards = input().split()
count_of_faro_shuffles = int(input())

for current_shuffle in range(count_of_faro_shuffles):

    middle_of_list = len(cards) // 2
    left_side = cards[:middle_of_list]
    right_side = cards[middle_of_list:]
    new_mixed_list = []

    for mixing in range(len(left_side)):
        new_mixed_list.append(left_side[mixing])
        new_mixed_list.append(right_side[mixing])

    cards=new_mixed_list

print(cards)
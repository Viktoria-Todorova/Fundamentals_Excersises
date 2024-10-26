seq_1 = input().split(", ")
seq_2 = input().split(", ")
new_list = []

for elements in seq_1:
    if any(elements in seq_item for seq_item in seq_2):
        new_list.append(elements)
print(new_list)

decorations = int(input())
days_till_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_gerland = 3
tree_lights = 15
final_price_of_orn = 0
shoping_points = 0
for days in range(1, days_till_christmas + 1):
    if days % 11 == 0:
        decorations += 2

    if days % 2 == 0:
        final_price_of_orn += decorations * ornament_set
        shoping_points += 5
    if days % 3 == 0:
        final_price_of_orn += decorations * (tree_skirt + tree_gerland)
        shoping_points += 13
    if days % 5 == 0:
        final_price_of_orn += decorations * tree_lights
        shoping_points += 17
        if days % 3 == 0:
            shoping_points += 30
    if days % 10 == 0:
        shoping_points -= 20
        final_price_of_orn += tree_skirt + tree_gerland + tree_lights


if days_till_christmas % 10 == 0:
    shoping_points -= 30

print(f"Total cost: {final_price_of_orn}")
print(f"Total spirit: {shoping_points}")

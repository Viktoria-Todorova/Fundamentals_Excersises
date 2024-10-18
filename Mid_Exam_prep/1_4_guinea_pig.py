food_per_kg = float(input())
hay_per_kg = float(input())
quantity_cover_kg = float(input())
guinies_weight = float(input())

food_per_gr = food_per_kg * 1000
hay_per_gr = hay_per_kg * 1000
quantity_cover_gr = quantity_cover_kg * 1000
guinies_weight_gr = guinies_weight * 1000
food = False
for day in range(1, 31):
    food_per_gr -= 300
    if food_per_gr <= 0:
        food = True
        break
    if day % 2 == 0:
        hay_per_gr -= (food_per_gr * 0.05)
        if hay_per_gr <= 0:
            food = True
            break
    if day % 3 == 0:
        quantity_cover_gr -= (guinies_weight_gr / 3)
        if quantity_cover_gr <= 0:
            food = True
            break
if food:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {(food_per_gr/1000):.2f}, Hay: {(hay_per_gr/1000):.2f}, Cover: {quantity_cover_gr/1000:.2f}.")




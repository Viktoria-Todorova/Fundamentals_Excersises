import re

number = int(input())
plants_info = {}
for info in range(number):
    current_info = input().split("<->")
    plant = current_info[0]
    rarity = int(current_info[1]) #
    if plant not in plants_info:
        plants_info[plant] = [rarity, []]  # Initialize rarity and an empty ratings list
    else:
        plants_info[plant][0] = rarity  # Update rarity if plant already exists



while True:
    command = input()
    if command == "Exhibition":
        break
    action, details = command.split(": ")
    plant_data = details.split(" - ")
    plant = plant_data[0]

    if action == "Rate":
        rating = int(plant_data[1])
        plants_info[plant][1].append(rating)  # Add rating to the list
    elif action == "Update":
        new_rarity = int(plant_data[1])
        plants_info[plant][0] = new_rarity
    elif action == "Reset":
        plants_info[plant][1] = []
    else:
        print("error")

print("Plants for the exhibition:")
for plant,(rarity,rating) in plants_info.items():
    avg_rating = sum(rating) / len(rating) if rating else 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")


animals = input().split(", ")
animals_list = animals[::-1] #reverse the list

find_index = animals_list.index("wolf")

if find_index == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {find_index}! You are about to be eaten by a wolf!")

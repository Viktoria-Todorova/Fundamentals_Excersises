budget = float(input())
kg_flour = float(input())

pack_of_eggs = kg_flour * 0.75
milk = kg_flour * 1.25
mil_for_bread = milk * 0.25

loafs = 0
loaf_price = pack_of_eggs + kg_flour + mil_for_bread
colored_eggs = 0
while budget >= loaf_price:
    colored_eggs += 3
    loafs += 1
    budget -= loaf_price

    if loafs % 3 == 0:
        colored_eggs -= (loafs - 2)

print(f"You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

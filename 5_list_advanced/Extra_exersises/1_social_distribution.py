population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
min_wealth = []
big_wealth = []
for distribution in range(len(population)):

    min_wealth = [min_w for min_w in population if int(min_w) < minimum_wealth]
    big_wealth = [big for big in population if int(big) >= minimum_wealth]
    for num in min_wealth:
       pass



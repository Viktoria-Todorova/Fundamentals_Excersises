capacity = 255
lines = int(input())
final_capacity = 0

for pouring in range(lines):
    litres = int(input())

    if capacity >= litres:
        capacity -= litres
        final_capacity += litres
    elif capacity < litres:
        print("Insufficient capacity!")

print(f"{final_capacity}")


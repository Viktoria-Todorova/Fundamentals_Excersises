people_in_circle = input().split()
k = int(input())
executed = []
counter = 0
new_list = []
while len(people_in_circle) > 0:
    counter = (counter + k - 1) % len(people_in_circle)
    executed.append(people_in_circle.pop(counter))
print(f"[{','.join(executed)}]")





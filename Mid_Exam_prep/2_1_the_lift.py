
people_waiting = int(input())
current_state = list(map(int, input().split()))


for i in range(len(current_state)):
    # Space available in the current wagon
    availabe_space = 4 - current_state[i]

    if people_waiting >= availabe_space :
        # Fill the wagon with the available space
        current_state[i] += availabe_space
        people_waiting -= availabe_space

    else:
        # Add the remaining people to the current wagon
        current_state[i] += people_waiting
        people_waiting = 0

    if people_waiting == 0:
        break

# Check if there are empty spots or people still in queue
if people_waiting == 0 and any(wagon < 4 for wagon in current_state):
    print("The lift has empty spots!")
elif people_waiting > 0 and all(wagon == 4 for wagon in current_state):
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(" ".join(map(str, current_state)))

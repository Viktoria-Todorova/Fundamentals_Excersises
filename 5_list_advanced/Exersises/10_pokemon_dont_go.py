# Input sequence of distances
distances = list(map(int, input().split()))
total_sum_removed = 0

# Loop until the list becomes empty
while len(distances) > 0:
    # Read index to remove
    index = int(input())

    # Handle special cases where the index is out of bounds
    if index < 0:
        # Remove the first element and use the last element to replace it
        removed_element = distances[0]
        distances[0] = distances[-1]
    elif index >= len(distances):
        # Remove the last element and use the first element to replace it
        removed_element = distances[-1]
        distances[-1] = distances[0]
    else:
        # Normal case: remove the element at the given index
        removed_element = distances.pop(index)

    # Add the removed element to the total sum
    total_sum_removed += removed_element

    # Modify the rest of the elements in the list
    for i in range(len(distances)):
        if distances[i] <= removed_element:
            distances[i] += removed_element
        else:
            distances[i] -= removed_element

# Output the total sum of removed elements
print(total_sum_removed)

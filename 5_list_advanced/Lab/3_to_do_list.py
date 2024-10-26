# Initialize an empty list to store the to-do notes along with their importance
final_list = []

# Start an infinite loop to continuously receive input
while True:
    to_do_notes = input()  # Get input from the user (expected format: "importance-task")

    # Check if the input is "End", if so, break the loop and stop collecting input
    if to_do_notes == "End":
        break  # Exit the loop

    # Split the input string into importance and task at the "-" character
    importance, task = to_do_notes.split("-")

    # Convert the importance to an integer (to sort by it later) and add both to the final_list as a list [importance, task]
    final_list.append([int(importance), task])

# Sort the final_list by the first element (importance) in each sublist
# Use list comprehension to create a sorted list of only the tasks, ignoring the importance in the output
sorted_to_do_list = [task for importance, task in sorted(final_list)]

# Print the sorted list of tasks (without the importance values)
print(sorted_to_do_list)

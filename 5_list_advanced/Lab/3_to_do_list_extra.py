notes = [0] * 10  # Create a list with 10 elements, all initialized to 0

while True:
    command = input()  # Receive input from the user
    if command == "End":
        break  # Exit the loop if "End" is received

    tokens = command.split("-")  # Split the input into priority and note
    priority = int(tokens[0]) - 1  # Convert priority to 0-based index
    note = tokens[1]  # Get the note

    notes[priority] = note  # Replace the note at the given priority

# Filter out the empty slots (0) and print the final list of notes
final_notes = [note for note in notes if note != 0]
print(final_notes)

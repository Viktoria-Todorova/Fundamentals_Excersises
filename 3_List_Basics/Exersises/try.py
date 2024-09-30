# Step 1: Input parsing
fires_with_cells = input().split("#")  # Split the input by "#"
water = int(input())  # Total water available

# Step 2: Initialize variables to track total fire, effort, and cells put out
total_fire = 0
effort = 0
putted_cell_out = []

# Step 3: Iterate over each fire cell
for fire in fires_with_cells:
    # Split by " = " to get the fire type and the value
    fire_info = fire.split(" = ")
    fire_type = fire_info[0]  # Get the type of fire (High, Medium, Low)
    cell_value = int(fire_info[1])  # Get the integer value of the cell

    # Step 4: Check if the fire is valid based on its type and value
    if (fire_type == "High" and 81 <= cell_value <= 125) or \
            (fire_type == "Medium" and 51 <= cell_value <= 80) or \
            (fire_type == "Low" and 1 <= cell_value <= 50):

        # Step 5: Check if we have enough water to put out the fire
        if water >= cell_value:
            water -= cell_value  # Use the water to put out the fire
            total_fire += cell_value  # Add to total fire
            effort += cell_value * 0.25  # Calculate effort as 25% of cell_value
            putted_cell_out.append(cell_value)  # Add the cell to the list of put out fires

# Step 6: Output the results
print("Cells:")
for cell in putted_cell_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

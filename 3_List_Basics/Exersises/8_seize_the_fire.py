fires_with_cells = input().split("#")
water = int(input())

total_fire = 0
effort = 0
putted_cell_out = []

for fire in fires_with_cells:
    fire_info = fire.split(" = ")

    current_type_fire = fire_info[0]

    current_value_int = int(fire_info[1])

    if (current_type_fire == "High" and 81 <= current_value_int <= 125) or \
            (current_type_fire == "Medium" and 51 <= current_value_int <= 80) or \
            (current_type_fire == "Low" and 1 <= current_value_int <= 50):
            if water >= current_value_int:
                water -= current_value_int
                effort += current_value_int / 4
                total_fire += current_value_int
                putted_cell_out.append(current_value_int)
print("Cells:")
for cell in putted_cell_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")



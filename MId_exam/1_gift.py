size_of_sides = float(input())
num_papers = int(input())
area = size_of_sides ** 2  * 6
total_area = 0
for each_sheet in range(1, num_papers + 1):
    lenght = float(input())
    width = float(input())
    area_of_paper = lenght * width

    if each_sheet % 3 == 0:
        area_of_paper -= area_of_paper * 0.25

    if each_sheet % 5 == 0:
        area_of_paper = 0

    total_area += area_of_paper


if total_area < area:
    final = total_area / area * 100
    print(f"You are out of paper!\n{(100-final):.2f}% of the box is not covered.")
else:
    final = ((total_area-area) / total_area) * 100
    print(f"You've covered the gift box!\n{final:.2f}% wrap paper left.")






numbers = input().split(", ")
boundary = 10

while numbers:
    filtering_nums_for_current =[ num for num in numbers if int(num) <= boundary]
    print(f"Group of {boundary}'s: [{', '.join(filtering_nums_for_current)}]"
)
    numbers = [numb for numb in numbers if numb not in filtering_nums_for_current]
    boundary += 10






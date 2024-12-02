the_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    text = command.split()
    current_command = text[0]

    if current_command == "exchange":
        index = int(text[1])
        if 0 <= index < len(the_list):
            the_list = the_list[index + 1:] + the_list[:index + 1]
        else:
            print("Invalid index")

    elif current_command == "max":
        max_or_odd = text[1]
        if max_or_odd == "odd":
            odd = [num for num in the_list if num % 2 != 0]
            if odd:
                max_odd = max(odd)
                print(len(the_list) - 1 - the_list[::-1].index(max_odd))  # Rightmost index
            else:
                print("No matches")
        elif max_or_odd == "even":
            even = [num for num in the_list if num % 2 == 0]
            if even:
                max_even = max(even)
                print(len(the_list) - 1 - the_list[::-1].index(max_even))  # Rightmost index
            else:
                print("No matches")

    elif current_command == "min":
        min_orodd = text[1]
        if min_orodd == "odd":
            odd = [num for num in the_list if num % 2 != 0]
            if odd:
                min_odd = min(odd)
                print(len(the_list) - 1 - the_list[::-1].index(min_odd))  # Rightmost index
            else:
                print("No matches")
        elif min_orodd == "even":
            even = [num for num in the_list if num % 2 == 0]
            if even:
                min_even = min(even)
                print(len(the_list) - 1 - the_list[::-1].index(min_even))  # Rightmost index
            else:
                print("No matches")

    elif current_command == "first":
        count = int(text[1])
        element = text[2]
        if count > len(the_list):
            print("Invalid count")
        else:
            if element == "even":
                filter_even = [num for num in the_list if num % 2 == 0]
                print(filter_even[:count])
            elif element == "odd":
                filter_odd = [num for num in the_list if num % 2 != 0]
                print(filter_odd[:count])

    elif current_command == "last":
        count = int(text[1])
        element = text[2]
        if count > len(the_list):
            print("Invalid count")
        else:
            if element == "even":
                filter_even = [num for num in the_list if num % 2 == 0]
                print(filter_even[-count:])
            elif element == "odd":
                filter_odd = [num for num in the_list if num % 2 != 0]
                print(filter_odd[-count:])

# Final output of the list
print(the_list)

list_of_int = input().split()
n = int(input())

list_to_int = []

# Convert the list of strings to a list of integers
for num in list_of_int:
    list_to_int.append(int(num))
# Sort the list and identify the smallest 'n' elements
sorted_list= sorted(list_to_int)
smalles_list = sorted_list[:n]
final_list = [] # Create a list for the remaining numbers, maintaining original order
for number in list_to_int:
    if number in smalles_list:
        sorted_list.remove(number) # Remove one occurrence of the smallest number
    else:
        final_list.append(number)

print(", ".join(map(str,final_list))) # Print the remaining numbers, separated by ", "


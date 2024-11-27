command = input()
contact_with_num = {}
while "-"  in command:
    contact = command.split("-")
    cont = contact[0]
    phone = contact[1]
    if cont not in contact_with_num:
        contact_with_num[cont] = 0
    contact_with_num[cont] =phone

    command = input()

number = int(command)

for i in range(number):
    current_name = input()
    if current_name in contact_with_num.keys():
        print(f"{current_name} -> {contact_with_num[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
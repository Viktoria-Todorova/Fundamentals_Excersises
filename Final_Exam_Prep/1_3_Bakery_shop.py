shop_stock = {}

sold = 0
while True:
    command = input()

    if command == "Complete":
        break

    command_to_parts =command.split()
    com =command_to_parts[0]
    quantity = int(command_to_parts[1])
    food = command_to_parts[2]

    if com == "Receive":
        if quantity > 0:  # Ignore invalid quantities
            if food not in shop_stock:
                shop_stock[food] = 0  # Add new food to stock
            shop_stock[food] += quantity

    if com == "Sell":

        if food not in shop_stock:
            print(f"You do not have any {food}.")

        else:
            if quantity > shop_stock[food]:

                print(f"There aren't enough {food}. You sold the last {shop_stock[food]} of them.")
                sold +=shop_stock[food] # Add all stock to sold
                del shop_stock[food]
            else:
                sold += quantity
                shop_stock[food] -= quantity

                print(f"You sold {quantity} {food}.")
                if shop_stock[food] == 0:
                    del shop_stock[food]

for food in shop_stock:
    print(f"{food}: {shop_stock[food]}")
print(f"All sold: {sold} goods")



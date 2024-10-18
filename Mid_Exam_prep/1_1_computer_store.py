command = input()
price_without_tax = 0

while command !="special" and command !="regular":
    price = float(command)
    if price < 0:
        print("Invalid price!")
    else:
        price_without_tax += price

    command = input()

if price_without_tax == 0:
    print("Invalid order!")
else:
    price_with_tax = price_without_tax * 1.2

    if command == "special":
        price_with_tax -= price_with_tax * 0.1

    tax = price_without_tax * 0.2

    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_tax:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {price_with_tax:.2f}$")

number_of_orders = int(input())
total_price = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    price_coffe = price_per_capsule * days * capsules_per_day

    if (2000 >= capsules_per_day >= 1) and (1 <= days <= 31) and (100 >= price_per_capsule >= 0.01):
        print(f"The price for the coffee is: ${price_coffe:.2f}")

        total_price += price_coffe

print(f"Total: ${total_price:.2f}")
items_with_price = input().split("|")
budget = int(input())
total_price = 0
money_spend = 0
list_selling_prices = []
for buying in items_with_price:
    buying_info = buying.split("->")
    item = buying_info[0]
    price = float(buying_info[1])


    if (item == "Clothes" and price <= 50) or \
            (item == "Shoes" and price <= 35) or \
            (item == "Accessories" and price <= 20.50):
        if price <= budget:
            budget -= price
            money_spend += price
            current_item_sell= price * 1.4
            formated_current = f"{current_item_sell:.2f}"
            total_price += current_item_sell
            list_selling_prices.append(formated_current)
profit = total_price - money_spend
profit_formated = f"{profit:.2f}"
total_money = budget + total_price

print(" ".join(list_selling_prices))
print(f"Profit: {profit_formated}")
if total_money > 150:
    print("Hello, France!")
else:
    print("Not enough money.")



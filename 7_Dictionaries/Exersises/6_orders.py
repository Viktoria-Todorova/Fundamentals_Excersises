items = {}
while True:
    product_info = input()

    if product_info == "buy":
        break
    product_info_ = product_info.split()

    name = product_info_[0]
    price = float(product_info_[1])
    quantity = int(product_info_[2])
    #If the product doesn't exist yet, add it with its starting quantity.
    if name not in items:
        items[name] = {
                'price': price,
                'quantity': quantity
            }
    #If you receive a product, that already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
    else:
        items[name]['quantity'] += quantity

        if items[name]['price'] != price:
            items[name]['price'] = price


for key, value in items.items():
    total_price = value['price'] * value['quantity']
    print(f'{key} -> {total_price:.2f}')

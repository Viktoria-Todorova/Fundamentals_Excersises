import re

number = int(input())
pattern = r'@(#+)([A-Z][A-Za-z0-9]{4,}[A-Z])@#+'
for barcodes in range(number):
    current_barcode = input()
    matches = re.fullmatch(pattern, current_barcode)
    if matches:
        barcode = matches.group(2)
        product_group = ""
        for char in barcode:
            if char.isdigit():
                product_group += char
        if not product_group:
            product_group = "00"

        print(f"Product group: {product_group}")


    else:
        print("Invalid barcode")


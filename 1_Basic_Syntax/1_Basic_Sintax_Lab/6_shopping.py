budget = int(input())

while True:
    prices = input()

    if prices == "End":
        print("You bought everything needed.")
        break

    price_c = int(prices)
    budget -= price_c

    if budget < 0:
        print("You went in overdraft!")
        break




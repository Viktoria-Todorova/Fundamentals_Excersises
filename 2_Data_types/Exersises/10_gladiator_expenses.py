lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
final_price = 0
for games in range(1,lost_fights+1):
    if games % 2 == 0:
        final_price += helmet_price
    if games % 3 == 0:
        final_price += sword_price
    if games % 6 == 0:
        final_price += shield_price
    if games % 12 == 0:
        final_price += armor_price

print(f"Gladiator expenses: {final_price:.2f} aureus")
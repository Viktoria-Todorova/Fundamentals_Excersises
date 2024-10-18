days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
plunder_gathered = 0
for day in range(1,days+1):
    plunder_gathered += daily_plunder
    if day % 3 == 0:
        plunder_gathered += daily_plunder * 0.5
    if day % 5 == 0:
        plunder_gathered *= 0.70



percentage = (plunder_gathered / expected_plunder) * 100
if plunder_gathered >= expected_plunder:
    print(f"Ahoy! {plunder_gathered:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")
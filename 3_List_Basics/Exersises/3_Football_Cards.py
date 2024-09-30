
football_players = input().split()
game_flag = False
team_a = [f"A-{team_number}"  for team_number in range(1,12)]
team_b = [f"B-{team_number}"  for team_number in range(1,12)]

for red_card in football_players:

    if red_card in team_a:
        team_a.remove(red_card)
    elif red_card in team_b:
        team_b.remove(red_card)
    else:
        pass
    if len(team_a) < 7 or len(team_b) < 7:
        game_flag =True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_flag:
    print("Game was terminated")






import math
num_of_tournaments = int(input())
points_in_rank_list = int(input())

tournament_points = 0
win = 0

for tournaments in range(1, num_of_tournaments + 1):
    stage_of_tournament = str(input())
    if stage_of_tournament == "W":
        points_in_rank_list += 2000
        tournament_points += 2000
        win += 1
    elif stage_of_tournament == "F":
        points_in_rank_list += 1200
        tournament_points += 1200
    elif stage_of_tournament == "SF":
        points_in_rank_list += 720
        tournament_points += 720

average_points = tournament_points / num_of_tournaments
percent_wins = win / num_of_tournaments * 100

print(f"Final points: {points_in_rank_list}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percent_wins:.2f}%")

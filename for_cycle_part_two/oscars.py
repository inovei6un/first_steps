name_of_actor = str(input())
academy_points = float(input())
number_of_judges = int(input())

judge_name = 0
points_given = 0
overall_points = 0
judge_points = 0

for judges in range(1, number_of_judges + 1):
    judge = str(input())
    judge_name = len(judge)
    points_given = float(input())
    judge_points += (judge_name * points_given / 2)
    overall_points = judge_points + academy_points

    if overall_points >= 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {overall_points:.1f}!")
        break
    else:
        pass

if overall_points < 1250.5:
    print(f"Sorry, {name_of_actor} you need {abs(1250.5 - overall_points):.1f} more!")

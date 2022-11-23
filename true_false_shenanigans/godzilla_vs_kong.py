budget = float(input())
extras = int (input())
extra_clothing = float(input())

decor = 0.10 * budget
clothes = extras * extra_clothing

if extras > 150:
    discount_for_clothes = 0.10 * clothes
    clothed_extras = clothes - discount_for_clothes
    sum_for_movie = decor + clothed_extras
else:
    clothed_extras = extras * extra_clothing
    sum_for_movie = decor + clothed_extras

if sum_for_movie > budget:
    print("Not enough money!")
    print('Wingard needs', f"{sum_for_movie - budget:.2f}", "leva more.")
else:
    print("Action!")
    print("Wingard starts filming with", f"{budget - sum_for_movie:.2f}", "leva left.")
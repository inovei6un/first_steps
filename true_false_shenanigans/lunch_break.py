name_of_series = str(input())
episode_continuity = int(input())
lunch_break = int(input())

import math

time_for_lunch = (1 / 8) * lunch_break
time_for_relax = (1 / 4) * lunch_break

time_for_everything = time_for_lunch + time_for_relax + episode_continuity

if lunch_break >= time_for_everything:
    print(f'You have enough time to watch {name_of_series} and left with {math.ceil(lunch_break - time_for_everything)} minutes free time.')
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {math.ceil(abs(time_for_everything - lunch_break))} more minutes.")

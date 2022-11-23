steps_needed = 10000
steps = 0
sum_steps = 0
is_goal_reached = False
command = input()

while command != "Going home":
    steps = int(command)
    sum_steps += steps
    if sum_steps >= steps_needed:
        is_goal_reached = True
        break
    command = input()
if command == "Going home":
    steps_until_home = int(input())
    sum_steps += steps_until_home
    if sum_steps >= steps_needed:
        is_goal_reached = True
if is_goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{abs(sum_steps - steps_needed)} steps over the goal!")
else:
    print(f"{abs(steps_needed - sum_steps)} more steps to reach goal.")

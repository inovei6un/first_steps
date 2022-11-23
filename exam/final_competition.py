dancers_number = int(input())
points_number = float(input())
season = input()
place = input()
reward = 0
final_reward = 0

if place == "Bulgaria":
    reward = points_number * dancers_number
    if season == "summer":
        final_reward = reward - 0.05 * reward
    elif season == "winter":
        final_reward = reward - 0.08 * reward
elif place == "Abroad":
    reward = points_number * dancers_number
    final_reward = reward + 0.5 * reward
    if season == "summer":
        final_reward = final_reward - 0.1 * final_reward
    elif season == "winter":
        final_reward = final_reward - 0.15 * final_reward

reward_after_charity = final_reward - 0.75 * final_reward

print(f"Charity - {0.75 * final_reward:.2f}")
print(f"Money per dancer - {reward_after_charity / dancers_number:.2f}")
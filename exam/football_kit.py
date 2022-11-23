shirt_price = float(input())
sum_needed = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
football_shoes_price = (shirt_price + shorts_price) * 2

sum_all = shirt_price + shorts_price + socks_price + football_shoes_price
sum_all_discounted = sum_all - 15 / 100 * sum_all

if sum_all_discounted >= sum_needed:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {sum_all_discounted:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {sum_needed - sum_all_discounted:.2f} lv. more.")

age_of_lily = int(input())
washing_machine_price = float(input())
price_for_toy = int(input())

money_saved = 0
toy_number = 0
money_increase = 0

for birthday in range(1, age_of_lily + 1):
    if birthday % 2 == 0:
        money_increase += 10
        money_saved += money_increase
        money_saved -= 1
    else:
        toy_number += 1

all_saved_money = money_saved + toy_number * price_for_toy

if all_saved_money >= washing_machine_price:
    print(f"Yes! {(all_saved_money - washing_machine_price):.2f}")
else:
    print(f"No! {abs(washing_machine_price - all_saved_money):.2f}")

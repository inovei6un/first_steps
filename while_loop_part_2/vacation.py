needed_money_for_vacation = float(input())
available_money = float(input())
has_saved = True
day_counter = 0
spending_counter = 0
while available_money < needed_money_for_vacation and spending_counter < 5:
    save_or_spend = input()
    saved_or_spent_money = float(input())
    day_counter += 1
    if save_or_spend == "spend":
        available_money -= saved_or_spent_money
        spending_counter += 1
        if available_money < 0:
            available_money = 0
    else:
        available_money += saved_or_spent_money
        spending_counter = 0
    if spending_counter == 5:
        has_saved = False
        break
    if available_money >= needed_money_for_vacation:
        has_saved = True
        break
if has_saved:
    print(f"You saved the money for {day_counter} days.")
else:
    print("You can't save the money.")
    print(day_counter)

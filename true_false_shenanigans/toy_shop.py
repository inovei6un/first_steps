vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
toy_trucks = int(input())

sum_all = (puzzles * 2.60) + (talking_dolls * 3) + (teddy_bears * 4.10) + (minions * 8.20) + (toy_trucks * 2)
number_of_toys = puzzles + talking_dolls + teddy_bears + minions + toy_trucks

if number_of_toys >= 50:
    discount = 0.25 * sum_all
    final_price = sum_all - discount
    rent = 0.1 * final_price
    money_won = final_price - rent
else:
    rent = 0.1 * sum_all
    money_won = sum_all - rent

enough_money = abs(money_won - vacation_price)
not_enough_money = vacation_price - money_won

if money_won >= vacation_price:
    print("Yes!", f'{enough_money:.2f}', "lv left.")
else:
    print("Not enough money!", f'{not_enough_money:.2f}', "lv needed.")

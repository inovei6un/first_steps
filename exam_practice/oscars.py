rent_price = float(input())

statue_price = rent_price - (30 / 100) * rent_price
catering = statue_price - (15 / 100) * statue_price
surround_sound = 1 / 2 * catering

sum_all = statue_price + catering + surround_sound + rent_price
print(f"{sum_all:.2f}")

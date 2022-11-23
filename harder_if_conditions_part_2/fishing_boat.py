budget = int(input())
season = str(input())
num_fishermen = int(input())
rent_price = 0

if num_fishermen <= 6:
    if season == "Spring":
        rent_price = 3000
        rent_price = rent_price - 0.1 * rent_price
    elif season == "Summer":
        rent_price = 4200
        rent_price = rent_price - 0.1 * rent_price
    elif season == "Autumn":
        rent_price = 4200
        rent_price = rent_price - 0.1 * rent_price
    elif season == "Winter":
        rent_price = 2600
        rent_price = rent_price - 0.1 * rent_price
if 7 <= num_fishermen <= 11:
    if season == "Spring":
        rent_price = 3000
        rent_price = rent_price - 0.15 * rent_price
    elif season == "Summer":
        rent_price = 4200
        rent_price = rent_price - 0.15 * rent_price
    elif season == "Autumn":
        rent_price = 4200
        rent_price = rent_price - 0.15 * rent_price
    elif season == "Winter":
        rent_price = 2600
        rent_price = rent_price - 0.15 * rent_price
if num_fishermen > 12:
    if season == "Spring":
        rent_price = 3000
        rent_price = rent_price - 0.25 * rent_price
    elif season == "Summer":
        rent_price = 4200
        rent_price = rent_price - 0.25 * rent_price
    elif season == "Autumn":
        rent_price = 4200
        rent_price = rent_price - 0.25 * rent_price
    elif season == "Winter":
        rent_price = 2600
        rent_price = rent_price - 0.25 * rent_price
if season == "Spring" or season == "Summer" or season == "Winter":
    if num_fishermen % 2 == 0:
        rent_price = rent_price - 0.05 * rent_price
else:
    pass

if budget >= rent_price:
    print(f"Yes! You have {budget - rent_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(rent_price - budget):.2f} leva.")

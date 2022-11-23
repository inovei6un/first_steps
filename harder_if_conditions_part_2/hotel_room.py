month = str(input())
nights_spent = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50 * nights_spent
    apartment = 65 * nights_spent
    if 7 < nights_spent < 14:
        studio = studio - 5 / 100 * studio
    elif 14 < nights_spent:
        studio = studio - 30 / 100 * studio
    if nights_spent > 14:
        apartment = apartment - 10 / 100 * apartment
if month == "June" or month == "September":
    studio = 75.20 * nights_spent
    apartment = 68.70 * nights_spent
    if nights_spent > 14:
        studio = studio - 20 / 100 * studio
    if nights_spent > 14:
        apartment = apartment - 10 / 100 * apartment
if month == "July" or month == "August":
    studio = 76 * nights_spent
    apartment = 77 * nights_spent
    if nights_spent > 14:
        apartment = apartment - 10 / 100 * apartment

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")

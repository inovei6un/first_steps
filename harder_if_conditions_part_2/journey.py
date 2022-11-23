budget = float(input())
season = str(input())

destination = 0
type_of_journey = 0
price = 0

if season == "summer":
    type_of_journey = "Camp"
    if budget <= 100:
        destination = "Bulgaria"
        price = 30 / 100 * budget
    if 100 < budget <= 1000:
        destination = "Balkans"
        price = 40 / 100 * budget
if season == "winter":
    type_of_journey = "Hotel"
    if budget <= 100:
        destination = "Bulgaria"
        price = 70 / 100 * budget
    if 100 < budget <= 1000:
        destination = "Balkans"
        price = 80 / 100 * budget
if budget > 1000:
    destination = "Europe"
    price = 90 / 100 * budget
    type_of_journey = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_journey} - {price:.2f}")

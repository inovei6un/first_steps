staying_days = int(input())
type_of_room = str(input())
rating = str(input())

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
night_at_hotel = staying_days - 1
price = 0
final_price = 0

if type_of_room == "room for one person":
    if night_at_hotel < 10:
        final_price = room_for_one_person * night_at_hotel
    if 10 <= night_at_hotel <= 15:
        final_price = room_for_one_person * night_at_hotel
    if night_at_hotel > 15:
        final_price = room_for_one_person * night_at_hotel

if type_of_room == "apartment":
    price = apartment * night_at_hotel
    if night_at_hotel < 10:
        final_price = price - 0.3 * price
    if 10 <= night_at_hotel <= 15:
        final_price = price - 0.35 * price
    if night_at_hotel > 15:
        final_price = price - 0.5 * price

if type_of_room == "president apartment":
    price = president_apartment * night_at_hotel
    if night_at_hotel < 10:
        final_price = price - 0.1 * price
    if 10 <= night_at_hotel <= 15:
        final_price = price - 0.15 * price
    if night_at_hotel > 15:
        final_price = price - 0.2 * price

if rating == "positive":
    final_price = final_price + 0.25 * final_price
elif rating == "negative":
    final_price = final_price - 0.1 * final_price

print(f'{final_price:.2f}')

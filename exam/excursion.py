number_of_people_in_group = int(input())
number_of_nights_spent = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

night_price = 20
transport_price = 1.60
museum_price = 6

nights_spent_price = number_of_nights_spent * night_price
transport_card_price = number_of_transport_cards * transport_price
museum_ticket_price = number_of_museum_tickets * museum_price

sum_all = (nights_spent_price + transport_card_price + museum_ticket_price) * number_of_people_in_group
sum_with_expenses = sum_all + (25 / 100 * sum_all)
print(f"{sum_with_expenses:.2f}")

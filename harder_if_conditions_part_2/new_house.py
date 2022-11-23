flower_type = str(input())
num_of_flowers = int(input())
budget = int(input())

final_price = 0
rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

if flower_type == "Roses":
    final_price = 5 * num_of_flowers
    if num_of_flowers > 80:
        rose_price = 5 * num_of_flowers
        final_price = rose_price - (10 / 100 * rose_price)
if flower_type == "Dahlias":
    final_price = 3.80 * num_of_flowers
    if num_of_flowers > 90:
        dahlia_price = 3.80 * num_of_flowers
        final_price = dahlia_price - (15 / 100 * dahlia_price)
if flower_type == "Tulips":
    final_price = 2.80 * num_of_flowers
    if num_of_flowers > 80:
        tulip_price = 2.80 * num_of_flowers
        final_price = tulip_price - (15 / 100 * tulip_price)
if flower_type == "Narcissus":
    final_price = 3 * num_of_flowers
    if num_of_flowers < 120:
        narcissus_price = 3 * num_of_flowers
        final_price = narcissus_price + 15 / 100 * narcissus_price
if flower_type == "Gladiolus":
    final_price = 2.50 * num_of_flowers
    if num_of_flowers < 80:
        gladiolus_price = 2.50 * num_of_flowers
        final_price = gladiolus_price + 20 / 100 * gladiolus_price

if budget >= final_price:
    print(f"Hey, you have a great garden with {num_of_flowers} {flower_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - final_price):.2f} leva more.")

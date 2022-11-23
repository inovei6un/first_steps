nylon = 1.50
paint = 14.50
diluent = 5.00

necessary_nylon = int(input())
necessary_paint = int(input())
necessary_diluent = int(input())
hours_for_work = int(input())

price_for_nylon = (necessary_nylon + 2) * nylon
price_for_paint = (necessary_paint + 10 / 100 * necessary_paint) * paint
price_for_diluent = (necessary_diluent * diluent)
price_for_bag = 0.40

sum_for_materials = price_for_nylon + price_for_paint + price_for_diluent + price_for_bag
sum_for_work = (sum_for_materials * (30 / 100)) * hours_for_work

final_sum = sum_for_materials + sum_for_work

print(final_sum)
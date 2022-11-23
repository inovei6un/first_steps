square_meters_to_be_greened = float(input())
price_per_square_meter = 7.61

whole_yard = square_meters_to_be_greened * price_per_square_meter
whole_yard_discount = (18 / 100) * whole_yard

whole_yard_with_discount = whole_yard - whole_yard_discount

print(f"The final price is {whole_yard_with_discount} lv.")
print(f"The discount is {whole_yard_discount} lv.")
projection_type = str(input())
rows = int(input())
columns = int(input())
price_for_projection = 0

if projection_type == "Premiere":
    price_for_projection = 12.00
elif projection_type == "Normal":
    price_for_projection = 7.50
elif projection_type == "Discount":
    price_for_projection = 5.00
else:
    pass

price_for_whole_saloon = rows * columns * price_for_projection

print(f'{price_for_whole_saloon:.2f}')

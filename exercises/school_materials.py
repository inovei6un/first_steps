pen_package = 5.80
marker_package = 7.20
detergent = 1.20

num_pen_package = int(input())
num_marker_package = int(input())
litres_detergent = int(input())
discount = int(input())

pen_price = num_pen_package * pen_package
marker_price = num_marker_package * marker_package
detergent_price = litres_detergent * detergent

sum_all = pen_price + marker_price + detergent_price

discount_price = sum_all - (sum_all * (discount / 100))

print(discount_price)
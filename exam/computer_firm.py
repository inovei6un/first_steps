pc_number = int(input())
number_of_sales = 0
average_rating = 0

for number in range(1, pc_number + 1):
    possible_sales_and_rating = int(input())
    last_digit = possible_sales_and_rating % 10
    possible_sales = int(str(possible_sales_and_rating)[:-1])
    if last_digit == 2:
        possible_sales = 0
    elif last_digit == 3:
        possible_sales = 1 /2 * possible_sales
    elif last_digit == 4:
        possible_sales = 0.7 * possible_sales
    elif last_digit == 5:
        possible_sales = 0.85 * possible_sales
    elif last_digit == 6:
        possible_sales = possible_sales
    number_of_sales += possible_sales
    average_rating += last_digit
average_rating_sum = average_rating / number
print(f"{number_of_sales:.2f}")
print(f"{average_rating_sum:.2f}")

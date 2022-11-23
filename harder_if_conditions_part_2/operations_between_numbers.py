number_one = int(input())
number_two = int(input())
operator = input()

result = 0
odd_even = 0

if operator == "+":
    result = number_one + number_two
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"{number_one} {operator} {number_two} = {number_one + number_two} - {odd_even}")
elif operator == "-":
    result = number_one - number_two
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"{number_one} {operator} {number_two} = {number_one - number_two} - {odd_even}")
elif operator == "*":
    result = number_one * number_two
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"{number_one} {operator} {number_two} = {number_one * number_two} - {odd_even}")
if operator == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        print(f'{number_one} / {number_two} = {number_one / number_two:.2f}')
if operator == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        print(f"{number_one} % {number_two} = {number_one % number_two}")

count_of_numbers = int(input())

even_sum = 0
odd_sum = 0

for numbers in range(count_of_numbers):
    numbers_input = int(input())
    if numbers % 2 == 0:
        even_sum += numbers_input
    else:
        odd_sum += numbers_input
if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")

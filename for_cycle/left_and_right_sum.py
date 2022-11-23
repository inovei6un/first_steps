n_numbers = int(input())

left_sum = 0
right_sum = 0

for left in range(n_numbers):
    l_number = int(input())
    left_sum += l_number
for right in range(n_numbers):
    r_number = int(input())
    right_sum += r_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")

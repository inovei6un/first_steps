import sys

count_of_numbers = int(input())
min_number = sys.maxsize
max_number = - sys.maxsize

for numbers in range(count_of_numbers):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

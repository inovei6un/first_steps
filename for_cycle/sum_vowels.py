input_text = str(input())
total_sum = 0

for letter in input_text:
    if letter == "a":
        total_sum += 1
    if letter == "e":
        total_sum += 2
    if letter == "i":
        total_sum += 3
    if letter == "o":
        total_sum += 4
    if letter == "u":
        total_sum += 5

print(total_sum)

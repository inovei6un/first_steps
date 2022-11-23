number_of_groups = int(input())

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
total_people = 0

for group in range(1, number_of_groups + 1):
    number_of_people = int(input())
    total_people += number_of_people
    if number_of_people <= 5:
        group1 += number_of_people
    elif 5 < number_of_people <= 12:
        group2 += number_of_people
    elif 13 <= number_of_people <= 25:
        group3 += number_of_people
    elif 26 <= number_of_people <= 40:
        group4 += number_of_people
    elif number_of_people >= 41:
        group5 += number_of_people

group1 = group1 / total_people * 100
group2 = group2 / total_people * 100
group3 = group3 / total_people * 100
group4 = group4 / total_people * 100
group5 = group5 / total_people * 100

print(f"{group1:.2f}%")
print(f"{group2:.2f}%")
print(f"{group3:.2f}%")
print(f"{group4:.2f}%")
print(f"{group5:.2f}%")

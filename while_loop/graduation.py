name_of_student = input()
bad_tries = 0
current_class = 1
grade = 0
is_ejected = False

while current_class <= 12:
    current_grade = float(input())
    if current_grade < 4:
        bad_tries += 1
        if bad_tries == 2:
            is_ejected = True
            break
        continue
    current_class += 1
    grade += current_grade
if is_ejected:
    print(f"{name_of_student} has been excluded at {current_class} grade")
else:
    average_grade = grade / 12
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")

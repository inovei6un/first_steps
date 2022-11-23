bad_grade_count = int(input())
fails = 0
solved_questions = 0
grades_sum = 0
last_problem = ''
has_failed = True
while fails < bad_grade_count:
    name_of_question = input()
    if name_of_question == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        fails += 1
    solved_questions += 1
    grades_sum += grade
    last_problem = name_of_question
if has_failed:
    print(f"You need a break, {bad_grade_count} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_questions:.2f}")
    print(f"Number of problems: {solved_questions}")
    print(f"Last problem: {last_problem}")

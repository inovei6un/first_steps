command = str(input())
max_score = 0
max_name = ""
goals = 0
name_of_footballer = ""

while command != "END":
    name_of_footballer = str(command)
    goals = int(input())
    if goals > max_score:
        max_score = goals
        max_name = name_of_footballer
    if goals >= 10:
        break
    command = input()

print(f"{max_name} is the best player!")
if goals >= 3:
    print(f"He has scored {max_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_score} goals.")

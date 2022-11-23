start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
combination = 0
is_true = False
for one in range(start_of_interval, end_of_interval + 1):
    for two in range(start_of_interval, end_of_interval + 1):
        combination += 1
        if one + two == magic_number:
            is_true = True
            break
    if is_true:
        break
if is_true:
    print(f"Combination N:{combination} ({one} + {two} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
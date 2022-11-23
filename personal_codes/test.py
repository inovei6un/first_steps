elements = [i for i in input().split(' ')]
command = input()
number_of_moves = 0

while command != "end":
    expand_command = command.split(' ')
    index1 = int(expand_command[0])
    index2 = int(expand_command[1])
    number_of_moves += 1
    if index1 == index2 and index1 not in elements and index2 not in elements:
        print(f"Invalid input! Adding additional elements to the board")
        mid = len(elements) // 2
        elements.insert(mid, f"-{number_of_moves}a")
        elements.insert(mid, f"-{number_of_moves}a")
    print(elements[index1], elements[index2])
    break
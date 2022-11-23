width_of_place = int(input())
length_of_place = int(input())
height_of_place = int(input())

size_of_place = width_of_place * length_of_place * height_of_place

cardboard_boxes = 0
sum_cardboard_boxes = 0

is_size_enough = True

command = input()

while command != "Done":
    cardboard_boxes = int(command)
    sum_cardboard_boxes += cardboard_boxes
    if sum_cardboard_boxes > size_of_place:
        is_size_enough = False
        break
    command = input()
if not is_size_enough:
    print(f"No more free space! You need {abs(sum_cardboard_boxes - size_of_place)} Cubic meters more. ")
if is_size_enough:
    print(f"{size_of_place - sum_cardboard_boxes} Cubic meters left.")

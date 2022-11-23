number_of_floors = int(input())
number_of_rooms = int(input())
type_of_room = ""
for floors in range(number_of_floors, 0, -1):
    for rooms in range(number_of_rooms):
        if floors == number_of_floors:
            type_of_room = "L"
        elif floors % 2 == 0:
            type_of_room = "O"
        elif floors % 2 != 0:
            type_of_room = "A"
        print(f"{type_of_room}{floors}{rooms}", end=" ")
    print()

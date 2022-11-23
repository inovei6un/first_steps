width = int(input())
length = int(input())
pieces_of_cake_taken = input()
number_of_pieces = width * length

while pieces_of_cake_taken != "STOP":

    pieces_of_cake_taken = int(pieces_of_cake_taken)
    number_of_pieces -= pieces_of_cake_taken
    if number_of_pieces <= 0:
        print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
        break
    pieces_of_cake_taken = input()

if pieces_of_cake_taken == "STOP":
    print(f"{number_of_pieces} pieces are left.")

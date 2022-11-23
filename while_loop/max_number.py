import sys

command = input()
max_num = - sys.maxsize
while True:
    number = int(command)
    if number > max_num:
        max_num = number
    command = input()
    if command == "Stop":
        break
print(max_num)

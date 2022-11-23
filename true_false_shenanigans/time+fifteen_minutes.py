hour = int(input())
minutes = int(input())

minutes += 15
if minutes >= 60:
    hour += 1
    minutes = minutes % 60

if hour > 23:
    hour = 0

if minutes < 10:
    print(f'{hour}:0{minutes}')
if minutes >= 10:
    print(f'{hour}:{minutes}')

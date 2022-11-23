hour_of_the_exam = int(input())
minute_of_the_exam = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

hours = 0
minutes = 0
exam_time = minute_of_the_exam + hour_of_the_exam * 60
arrival_time = minute_of_arrival + hour_of_arrival * 60
difference = exam_time - arrival_time

if difference < 0:
    print("Late")
    difference = abs(difference)
    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{difference} minutes after the start")
elif 0 <= difference <= 30:
    print("On time")
    if difference > 0:
        print(f'{difference} minutes before the start')
elif difference > 30:
    print("Early")
    if difference >= 60:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{difference} minutes before the start")

page_count = int(input())
pages_per_hour = int(input())
number_of_days_to_read = int(input())

all_time_reading = page_count / pages_per_hour
needed_reading_hours = all_time_reading / number_of_days_to_read

print(round(needed_reading_hours))
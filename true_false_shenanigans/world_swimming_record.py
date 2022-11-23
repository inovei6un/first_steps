world_record_seconds = float(input())
distance_meters = float(input())
time_per_meter_swimming = float(input())

distance_to_swim_in_seconds = distance_meters * time_per_meter_swimming
water_resistance = (distance_meters // 15) * 12.5
time_sum = distance_to_swim_in_seconds + water_resistance

if world_record_seconds > time_sum:
    print(f'Yes, he succeeded! The new world record is {time_sum:.2f} seconds.')
else:
    print(f'No, he failed! He was {(abs(world_record_seconds - time_sum)):.2f} seconds slower.')

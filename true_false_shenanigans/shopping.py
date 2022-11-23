budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memories = int(input())

price_for_video_cards = video_cards * 250
price_for_processors = price_for_video_cards * 0.35
price_for_ram_memory = price_for_video_cards * 0.1

if video_cards > processors:
    final_sum = price_for_video_cards + (price_for_processors * processors) + (price_for_ram_memory * ram_memories)
    discount = 0.15 * final_sum
    final_sum = final_sum - discount
else:
    final_sum = (price_for_video_cards + (price_for_processors * processors) + (price_for_ram_memory * ram_memories))

if budget >= final_sum:
    print(f'You have {budget - final_sum:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(final_sum - budget):.2f} leva more!')

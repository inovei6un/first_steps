deck = [card for card in input().split(' ')]
shuffles = int(input())
length = len(deck)
mid = length // 2
shuffled_deck = list()

first_half = deck[:mid]
second_half = [card for card in deck if card not in first_half]

for i in range(1, shuffles + 1):
    shuffled_deck = [c for pair in zip(first_half, second_half) for c in pair]
    first_half.clear()
    second_half.clear()
    for num in range(len(shuffled_deck)):
        first_half = shuffled_deck[:mid]
        second_half = [card for card in shuffled_deck if card not in first_half]
print(shuffled_deck)

length = int(input())
width = int(input())
height= int(input())
percent = float(input())

capacity = length * width * height
capacity_in_litres = capacity / 1000
occupied_space = percent / 100

necessary_litres = capacity_in_litres * (1 - occupied_space)

print(necessary_litres)
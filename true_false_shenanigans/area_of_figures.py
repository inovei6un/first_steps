figure = str(input())
result = 0
if figure == "square":
    side = float(input())
    result = side * side
elif figure == "rectangle":
    side = float(input())
    side2 = float(input())
    result = side * side2
elif figure == "circle":
    side = float(input())
    import math
    result = math.pi * side * side
elif figure == "triangle":
    side = float(input())
    height = float(input())
    result = (side * height) / 2

print(f"{result:.3f}")

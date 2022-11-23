n = int(input())

for x3 in range(1, n % 10 + 1):
    for x2 in range(1, (n // 10) % 10 + 1):
        for x1 in range(1, n // 100 + 1):
            print(f"{x3} * {x2} * {x1} = {x1 * x2 * x3};")
command = input()
while command != "End":
    destination = command
    minimal_budget = float(input())
    sum_savings = 0
    while sum_savings < minimal_budget:
        savings = float(input())
        sum_savings += savings
    print(f"Going to {destination}!")
    command = input()

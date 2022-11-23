tabs_open = int(input())
salary = float(input())


for tabs in range(1, tabs_open + 1):
    tab = str(input())
    if tab == "Facebook":
        salary -= 150
    elif tab == "Instagram":
        salary -= 100
    elif tab == "Reddit":
        salary -= 50
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")

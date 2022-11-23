user_name = str(input())
password = input()
data = input()

while data != password:
    data = input()
print(f"Welcome {user_name}!")

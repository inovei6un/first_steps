deposit = float(input())
term = int(input())
yearly_interest_rate = float(input())

result = deposit + term * ((deposit * yearly_interest_rate / 100) / 12)
print(result)
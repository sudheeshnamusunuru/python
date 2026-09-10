#bitwise operators

a=5
b=3

print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)

#electricity bill calculator

units = int(input("Enter electricity units:"))

rate = 6

bill = units * rate
print("Electricity Bill:", bill)

#travel expense calculator

travel = float(input("Travel expense:"))
food = float(input("Food expense:"))
hotel = float(input("Hotel expense:"))

total = travel+food+hotel
print("Total Expense:",total)
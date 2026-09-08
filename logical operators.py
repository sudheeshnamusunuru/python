#logical operators

age=25
citizen=True
print(age>=18 and citizen == True)

age=16
citizen=True
print(age>=18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash)

is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balance=10000
withdraw=5000

print(withdraw>0 and withdraw <= balance)

#student scholarship eligibility checker

marks=float(input("Enter marks:"))
attendance = float(input("Enter attendance:"))

eligible = marks >= 85 and attendance >= 75

print("Scholarship Eligible:",eligible)


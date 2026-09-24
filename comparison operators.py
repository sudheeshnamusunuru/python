#comparison operators
a=10
b=20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#age eligibility checker

age=int(input("Enter your age:"))
print("Eligible:",age >= 18)

#pass or fail checker
marks=int(input("Enter marks:"))

print("Passed:", marks >= 40)

#login validation

correct_username = "admin"
correct_password = "1234"

username = input("Enter username:")
password = input("Enter password:")

print(username == correct_username)
print(password == correct_password)


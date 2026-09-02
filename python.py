#arithmetic operator
a=10
b=3

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Floor Division:",a//b)
print("Remainder:",a%b)
print("Powers:",a**b)

#simple calculator
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)

#student marks calculator

name=input("Enter student name:")
m1=int(input("Enter python marks:"))
m2=int(input("Enter Java marks:"))
m3=int(input("Enter SQL marks:"))

total=m1+m2+m3
average=total/3

print("\n-----Student Report-----")
print("Name:",name)
print("Total:",total)
print("Average:",average)

#shopping bill calculator
price1=float(input("Enter product1 price:"))
price2=float(input("Enter product2 price:"))
price3=float(input("Enter product3 price:"))
total=price1+price2+price3
discount=total*0.10
final_amount=total-discount
print("PRICE 1:",price1)
print("PRICE 2:",price2)
print("PRICE 3:",price3)
print("TOTAL:",total)
print("DISCOUNT:",discount)
print("FINAL_AMOUNT:",final_amount)

#salary calculator
basic=float(input("Enter basic salary:"))
hra=basic*0.20
da=basic*0.10

gross_salary=basic+hra+da

print("Basic salary:",basic)
print("HRA:,hra")
print("DA:",da)
print("Gross Salary:",gross_salary)
                  
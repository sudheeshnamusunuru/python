#control statements

#if statement:It executes the statement if the given condition is true.

age = 20
if age>=18:
    print("Eligible for vote")

number=int(input("Enter a number:"))
if number%5==0:
    print("Divisible by 5") 

#Temperature check
temperature=float(input("Enter temperature:"))
if temperature>40:
    print("High temperature")

#if-else statement:This condition is used when there are two possibilities.
age=18
if age>=20:
    print("Eligible")
else:
    print("not eligible")

marks=35
if marks>=45:
    print("Pass")
else:
    print("Fail")

#even or odd check
number = int(input("Enter a number:"))
if number%2==0:
    print("Even")
else:
    print("Odd")

#pass or fail check
marks = int(input("Enter marks:"))
if marks>=45:
    print("Pass")
else:
    print("Fail")

#positive or negative check
number = int(input("Enter a number:"))
if number>0:
    print("Positive")
else:
    print("Negative")

number = int(input("Enter a number:"))
if number>100:
    print("Number is greater than 100")
else:
    print("Number is not greater than 100")

#if elif else statement:used when more than 2 conditions are usec
marks = int(input("Enter marks:"))
if marks>=90:
    print("GradeA")
elif marks>=75:
    print("GradeB")
elif marks>=64:
    print("GradeC")
elif marks>=56:
    print("GradeD")
elif marks>=40:
    print("GradeE")
else:
    print("Fail")

#Largest of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a>b:
    print("Largest:",a)
elif b>a:
    print("Largest:",b)
else:
    print("Both numbers are equal")

#largest of three numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>=b and a>=c:
    print("Largest:",a)
elif b>=a and b>=c:
    print("Largest:",b)
else:
    print("Largest:",c)

number = int(input("Enter a number:"))
if number>0:
    print("positive")
elif number<0:
    print("negative")
else:
    print("Zero")

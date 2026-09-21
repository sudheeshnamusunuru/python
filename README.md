#Program 1:Display Personal Details Using Variables
#Getting the input from user
name = input("Enter your name:")
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))


#Printing the values
print(name)
print(age)
print(height)

#Program 2:Personalised Greeting
name=input("Enter your name:")
print(F"Hello,{name}!")

#Program 3:Add Two Numbers Read As Strings
#Taken the input as a string
a = input("Enter first number:")
b = input("Enter second number:")
#converting the string into integer
a = int(a)
b = int(b)
#Find the sum
total = a+b
#Print the result
print(total)


#Program 4:Float into integer Conversion
#float:numbers with decimal value
#int:Whole numbers without any decimal or fractional value
#Reading a float value from the user
n=float(input("Enter your marks:"))
#Print the float value
print(n)
#Convert the float into integer:Decimal point values will be removed
new = int(n)
#Print the result
print(new)


#Prograam 5:Sum using Arithmetic  Operator
#reading 2 integers from the user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
#Finding the sum and reading the result
print(a+b)


#Program 6:Area of a Rectangle
#Reading input from the user
length = float(input("Enter length:"))
breadth = float(input("Enter breadth:"))
#Calculating the area of a rectangle
area = length*breadth
#print the result
print(area)


#Program 7:Quotient and Remainder
#User inputs
a=int(input("Enter first number:")) 
b=int(input("Enter second number:"))
#find the quotient
q=a/b
#find the remainder
r=a%b
#Print the result
print(q)
print(r)


#Program 8:Power Calculation
#reading user input
base = int(input("Enter a number:"))
exponent = int(input("Enter a number:"))
#calculate the power and print the result
print(base**exponent)


#Program 9:Average of three numbers
#Taking 3 integer numbers from the user
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
n3 = int(input("Enter third number:"))
#Find the total
total = n1+n2+n3
#Find the average
avg = total/3 # Division Operator /-->always gives the result as a float.
#print the average
print(avg)


#Program 10:Greater than Comparison
#read 2 integer numbers from user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
#Check whether the 1st number is greater than the 2nd number
print(a>b)


#Program 11:Equality Check
#Check whether both the numbers are same or not
#If the numbers are same - True
#If the numbers are different - False
#Reading the input from the user
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print(n1==n2)


#Program 12;Both numbers positive check
#If the number is greater than 0
#Logical and-->If all combining conditions are True,the result is True
#Reading the input from the user
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print(n1>0 and n2>0)


#Program 13:Atleast one evn number
#Even number:If the number is divisible by 2(Without any remainder)
#Logical or -->If any one of the combining condition is True,then the result is True
#Arithmetic operators 
# /-->Divison - result is in the form of decimal value
#Example:13/2 = 6.5
#//-->Floor  Divison- result is in the form of integer
#Example:13/2 = 6
#%-->Modulo - result is the remainder of the divison operaton
#Example:13/2 = 1

#Reading the input from the user
n1=int(input("Enter first number:"))
n2=int(input("Enetr second number:"))
print(n1%2==0 or n2%2==0)


#Program 14:Logical NOT on a condition
#logical not -->reverse the result
#True-->False
#False-->True
#Reading the input from the user
num = int(input("Enter a number:"))
print(not(num>0))

#Program 15:Augumented assignment operations
#Read a number from the user
a=int(input("Enter a number:"))#20
a=a+5 # a = 20+5-->25
a=a*2 # a = 25*2-->50
a=a-3 # a = 50-3-->47
print(a)


#Program 16:Exchange values of two variables
#Reading the input from the user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

#Logic1-Using temp variable
temp=a
a=b
b=temp
print(a)
print(b)

#Logic2:Without using temp(3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)

#Logic3:Without using temp(3rd variable)
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#Logic4:Without using temp(3rd variable)
#Problem:It cannot handle 0
a=a*b
b=a/b
a=a/b
print(a)
print(b)

#Logic5:Using Python's special
#Simplest way
a,b = b,a
print(a)
print(b)


#Program 17:Calculate Simple Interest
#Formula:(Principle*Rate*Time)/100
#User inputs
principle = float(input("Enter principle value:"))#Loan amount
rate = float(input("Enter rate:"))#rate of interest
time = float(input("Enter time:"))#repayment time
#Calculate interest
si=(principle*rate*time)/100
#print the result
print(si)


#Program 18:Temperature Conversion(Celsius to Fahrenheit)
#Formula:F=(C*9/5)+32
#Read the temperature in celsius
c=float(input("Enter temperature in celsius:"))
#Convert the celsius to Fahrenheit
f=(c*9/5)+32
print(f)


#Program 19:Check divisibility by 3 and 5
n=int(input("Enter a number:"))
print(n%3==0 and n%5==0)


#Program 20:Sum of Digits of a Two-Digit number
num = int(input("Enter a number:")) #num=48
tens = num//10 #tens = 48//10 = 4
units = num%10 #units = 48%10 = 8
total = tens + units #total = 4+8 = 12

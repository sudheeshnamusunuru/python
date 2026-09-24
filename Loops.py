#Loops
#use for when you know how many times you want to repeat or when you want to iterate over a sequence
#Looping through numbers 1 to 5
for i in range(1,6):
    print(i)

#print numbers from 1 to 10
for i in range(1,11):
    print(i)

#print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#print even numbers from 2 to 50
for i in range(2,51,2):
    print(i)

#print odd numbers from 1 to 50
for i in range(1,50,2):
    print(i)

#print multiples of 5 from 5 to 50
for i in range(5,51,5):
    print(i)

#Multiplication table
number=int(input("Enter a number:"))
for i in range(1,11):
    print(number,"*",i,"=",number*i)

#Sum of numbers from 1 to n
n=int(input("Enter n: "))
total = 0
for i in range(1,n+1):
    total = total+i
print("Sum:",total)

#Factorial of a number
n=int(input("Enter number:"))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("Factorial:",factorial)

#Sum of even numbers from 2 to n
n = int(input("Emter n:"))
total=0
for i in range(2,n+1,2):
    total=total+i
print("Sum:",total)

#Count of multiples of 3
n=int(input("Enter n:"))
count=0
for i in range(1,n+1):
    if i%3==0:
        count=count+1
print("Count:",count)

#Sum of multiples of 5
n=int(input("Enter n:"))
total = 0
for i in range(1,n+1):
    if i%5==0:
        total=total+i
print("Sum:",total)

#use while when repitition depends on a condition.
#Looping through numbers 1 to 5 using whiile loop
i=1
while i<=5:
    print(i)
    i=i+1
#print all even numbers from 2 to 50 by using while loop
i=2
while i<=50:
    print(i)
    i=i+2
#print all odd numbers from 1 to 50 by using while loop
i=1
while i<=50:
    print(i)
    i=i+2
#Print total of numbers entered by user until the 0 is entered
total=0
number = int(input("Enter number:"))
while number !=0:
    total=total+number
    number = int(input("Enter number:"))
print("Total:",total)

#Count the number of digits in a number
n = int(input("Enter a number:"))
count=0
while n>0:
    count=count+1
    n=n//10
    print("Count:",count)

#Password check
password = ""
while password != "python123":
    password = input("Enter password:")
print("Login successful")

#Count the number of digits in a number
number = int(int(input("Enter number:")))
count=0
while number>0:
    number=number//10
    count=count+1
print("Number of digits:",count)

#Sum of digits in a number
number=int(input("Enter a number:"))
total=0
while number > 0:
    digit=number%10
    number=number//10
    total=total+digit
    print("Sum of digits:",total)

#Reverse a number
number = int(input("Enter number:"))
reverse=0
while number>0:
    digits=number%10
    number=number//10
    reverse=reverse*10+digit
print("Reverse:",reverse)

#Check if a number is a palindrome
number=int(input("Enter a number:"))
original=number
Reverse=0
while number>0:
    digits=number%10
    number=number//10
    reverse=reverse*10+digit
if original==number:
    print("Palindrome")
else:
    print("Not palindrome")

#Check if a number is prime
number=int(input("Enter a number:"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count==2:
    print("Prime Number") 
else:
    print("Not a prime number")

#Print all prime numbers between 2 to 100
for number in range(2,101):
    count=0
    for i in range(1,number+1):
        if number%1==0:
            count=count+1
    if count==2:
        print(number)       

#break
for i in range(1,15):
    if i==10:
        break #exit the loop
    print(i)

for i in range(1,11):
    if i==7:
        print("Number found")
        break
    print(i)

#Print numbers until user enter 0
while True:
    number = int(input("Enter number:"))
    if number==0:
        break
    print("You entered:",number)

#continue
for i in range(1,20):
    if i==15:
        continue #skip the current iteration and continue the next iteration
    print(i)

    #Print odd numbers from 1 to 10
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

  #Pass
for i in range(1,10):
    if i ==5:
        pass #nothing will do
    print(i)  

age=20
if age>=20:
    print("Eligible")
else:
    print("Not Eligible")

#Print numbers from 1 to 100 , but skip multiples of 3 and stop at 50
for i in range(1,101):
    if i==50:
        break
    if i % 3 == 0:
        continue
    print(i)

#Calculate the sum of positve numbers entered by the user
total=0
while True:
    number=int(input("Enter number:"))
    if number<0:
        continue
    if number==0:
        break
    total=total+number
    print("Total:",total)

    #Find the first number between 1 and 100 that is divisible by both 3 and 5
    for i in range(1,101):
        if i % 3== 0 and i % 5 == 0:
            print("First number:"i)
            break

#Calculate the sum of positive numbers entered by the user ignoriing negative numbers
total=0
for i in range(10):
    number = int(input("Enter number:"))
    if number<0:
        continue
    total=total+number
    print("Total:",total)

#password check with limited attempts
correct_password = "python123"
for attempt in range(1,4):
    password = input("Enter password:")
    if password==correct_password:
        print("Login successful")
        break
    print("Wrong password")
else:
    print("Account locked")

#Find the largest number among 5 numbers entered by the user
largest = None
for i in range(5):
    number = int(input("Enter number:"))
    if largest is None or number > largest:
        largest=number
print("Largest:",largest)

#Find the smallest number among 5 numbers entered by the user
smallest=None
for i in range(5):
    number=int(input("Enter number:"))
    if smallest is None or number<smallest:
        smallest=number
print("Smallest:",smallest)
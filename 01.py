
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

if(a>b):
    if(a>c):
        print(a,"is greater")
    else:
        print(c,"is greater")
elif(b>c):
    print(b,"is greater")
else:
    print(c,"is greater")

# ------------------------------------------------------

a = int(input("enter number: "))

if(a>0):
    print(a,"is positive")
elif(a<0):
    print(a,"is negetive")
else:
    print(a,"is zero")

# ------------------------------------------------------

a = int(input("enter number: "))

if(a%5==0):
    print(a,"is divisible by 5")
elif(a%11==0):
    print(a,"is divisible by 11")
else:
    print("not divisible by 5 or 11")

# -------------------------------------------------------

a = int(input("enter number: "))

if(a%2==0):
    print(a,"is even")
else:
    print(a,"is odd")

# -------------------------------------------------------
    
a = int(input("enter number: "))

if(a%400==0):
    print(a,"is a leap year")
elif(a%4==0):
    print(a,"is a leap year")
elif(a%100==0):
    print(a,"is a leap year")
else:
    print(a,"is not a leap year")

# --------------------------------------------------------
    
a = int(input("enter maths: "))
b = int(input("enter physics: "))
c = int(input("enter chemistry: "))
d = int(input("enter english: "))
e = int(input("enter hindi: "))

totel = (a+b+c+d+e)/5

print("total marks is",a+b+c+d+e)
print("total percentage is",totel)

if(totel>90):
    print("your grade is A")
elif(totel<=30):
    print("your grade is D")
elif(totel<=60):
    print("your grade is C")
elif(totel<=90):
    print("your grade is B")

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

a = int(input("enter your salary: "))
ba = int(input("enter your years in compony: "))

if(ba>5):
    print("your bonous is", 0.5*a)
else:
    print("you won't get bonous")

# Take values of length and breadth of a rectangle from user and check if it is square or not.

a = int(input("enter hight: "))
b = int(input("enter width: "))

if(a==b):
    print("it is a square as hight",a,"is equal to width",b)
else:
    print("is a rectangle")

# --------------------------------------------------------
    
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
if(current_time>"19:00:00"):
    print("Good Night Sir")
elif(current_time>"17:00:00"):
    print("Good Evening Sir")
elif(current_time>"12:00:00"):
    print("Good Afternoon Sir")
elif(current_time>"05:00:00"):
    print("Good Morning Sir")


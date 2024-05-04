# Questions form: https://codeforwin.org/c-programming/for-do-while-loop-programming-exercises

for i in range(1,11):
    print(i)

# ----------------------------------------------

a = int(input("enter Nth number:"))
for i in range(a):
    i = a - i
    print(i)

# ----------------------------------------------

for i in range(1,100):
    if(i%2==0):
        print(i,"is even")

# -----------------------------------------------

for i in range(1,100):
    if(i%2!=0):
        print(i,"is odd")

# -----------------------------------------------
        
n = int(input("enter Nth number:"))
sum = 0
for i in range(1,n):
    sum = sum + i

print(sum)

# ------------------------------------------------

n = int(input("enter Nth number:"))
evensum = 0
for i in range(1,n+1):
    if(i%2==0):
        evensum = evensum + i
    
print(evensum)

# -------------------------------------------------

n = int(input("enter Nth number:"))
oddsum = 0
for i in range(1,n+1):
    if(i%2!=0):
        oddsum = oddsum + i
    
print(oddsum)

# --------------------------------------------------

n = int(input("Enter Nth number:"))

for i in range(1,10+1):
    print(n,"x",i,"=",n*i)

# --------------------------------------------------
    
digit = input("enter digit:")
count = 0
for i in digit:
    count = count + 1
    
print(count)

# --------------------------------------------------

digit = input("enter digit:")
count = 0
for i in digit:
    count = i
print("First Digit: ",digit[0])
print("Last Digit: ",count)

# ---------------------------------------------------

digit = input("enter digit:")
count = 0
for i in digit:
    count = i
print("First Digit: ",digit[0])
print("Last Digit: ",count)
print("Sum Digit: ",int(digit[0])+int(count))

# ---------------------------------------------------

digit = input("enter digit:")
sum = 0
j = 0
for i in digit:
    j = int(i)
    sum = sum + j
print(sum)

# ----------------------------------------------------

digit = input("enter digit:")
sum = 1
j = 0
for i in digit:
    j = int(i)
    sum = sum * j
print(sum)

# ----------------------------------------------------


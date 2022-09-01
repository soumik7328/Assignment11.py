#Assignment - 11 Full Stack Web Development using Python MySirG loops
#1. Write a python script to calculate sum of first N natural numbers
a=eval(input("Enter a number "))
sum=0
for e in range(0,a+1):
    sum=sum+e
print(sum)
#2. Write a python script to calculate sum of squares of first N natural numbers
a=eval(input("Enter a number "))
sum=0
for e in range(0,a+1):
    sum=sum+(e**2)
print(sum)
#3. Write a python script to calculate sum of cubes of first N natural numbers
a=eval(input("Enter a number "))
sum=0
for e in range(0,a+1):
    sum=sum+(e**3)
print(sum)
#4. Write a python script to calculate sum of first N odd natural numbers
a=eval(input("Enter a number"))
sum=0
for e in range(1,(a*2)+1,2):
    sum=sum+e
print(sum)    
#5. Write a python script to calculate sum of first N even natural numbers
a=eval(input("Enter a number"))
sum=0
for e in range(2,(a*2)+1,2):
    sum=sum+e
print(sum)
#6. Write a python script to calculate factorial of a given number
num=int(input("Enetr a number:-"))
factorial=1
if num<0:
    print("Sorry!factorial does not exit for negetive number")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of", num , "is", factorial)            

#7. Write a python script to count digits in a given number
number=eval(input("Enter a number"))
c=0
for e in str(number):
    c=c+1
print(c)    
#8. Write a python script to calculate sum of digits of a given number
number=eval(input("Enter a number"))
sum=0
for e in str(number):
    sum=sum+int(e)
print(sum) 
#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
a=(input("Enter a bionary number"))
l=list(a)
l.reverse
decimal=0
for e in range(len(l)):
    decimal=decimal+int(l[e])*2**e
print("binary equivalent of a given decimal number",decimal)    
    

#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
octal=float(input("Enter a octal number:-"))
sum=0
i=0
while octal!=0:
    r=octal%10
    sum+=r*pow(8,i)
    i=i+1
    octal=int(octal/10)
print(sum)


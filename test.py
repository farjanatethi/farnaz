print("tethi \n 01324885282")
print("\"tethi \" ")
#variable
name ="mishu"
age=34
score=3.95
print("Our new student name " +name)
print("she is ", age,"years old")
print("Her Score is ",score)
#user input
user= input("enter your name:")
print("User name: "+user)
#type casting
num1=int (input("Enter the first num:"))
num2=int(input("Enter the second num:"))
result= num1-num2
print("the result is :",result)
#math
from math import *
print(min(34,50,67))
print(sqrt(30))
#string formatting
num1=20
num2=30
print(f"{num1}+{num2}={num1+num2}")
print("tethi moni",end=" ")
print(908084989)
#else if
mark=40
if mark>=33:
    print("pass")
else:
    print("faIL")

num5=50
if num5%2==0:
    print("even")
else:
    print("odd")
marks =60
if marks>=80:
    print("A+")
elif marks>=70:
    print("A")
elif marks>=60:
    print("A-")
else :
    print("F")
#nested if
num4=40
num5=50
num6=30
if num4>num5:
    if num4>num6:
        print(num4)
    else:
        print(num6)
else :
    if num5>num6:
        print(num5)
    else:
        print(num6)

#tarnery
num7=30
num8=70
max=num7 if num7>num8 else num8
print(max)
#logical opoeration
ch=input("Enter the character:")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("vowel")
else:
    print("consopnent")





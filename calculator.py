def add(num1,num2):
    add = num1+num2
    print(add)
def subtract(num1, num2):
    subtract = num1 - num2
    print(subtract)
def multiply(num1, num2):
    multiply = num1 * num2
    print(multiply)
def divide(num1,num2):
    divide = num1/num2
    print(divide)
def power(num1,num2):
    power=num1**num2
    print(power)
def remainder(num1,num2):
    remainder=num1%num2
    print(remainder)

num1 = int(input("Give me a random number"))
num2 = int(input("Give me a second random number"))
operation=input("Do you want to +,-,*,/,%,**")
if operation=="+" or operation=="add":
    add(num1,num2)
elif operation=="-" or operation=="subtract":
    subtract(num1,num2)
elif operation=="*" or operation=="multiply":
    multiply(num1,num2)
elif operation=="**" or operation=="power":
    power(num1,num2)  
elif operation=="/" or operation=="divide":
    divide(num1,num2)
elif operation=="%" or operation=="remainder":
    remainder(num1,num2)
else:
    print("I will come to your house and rip your vocal cords out!")

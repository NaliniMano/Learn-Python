input1=int(input("Enter number"))
input2=int(input("Enter number2"))
ops=input("Enter  a option = add sub mul div")
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return int(num1/num2)

if ops =="add":
    print(add(input1,input2))
if ops =="sub":
    print(sub(input1,input2))
if ops =="mul":
    print(mul(input1,input2))
if ops =="div":
    print(div(input1,input2))


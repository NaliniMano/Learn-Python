getinput=input("Enter number to find factorial = ")
number=int(getinput)
fact=1
for x in range(1,number+1):
    fact=fact*x
print("Factorial of Number",number,"=",fact)

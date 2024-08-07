#find factorial

get_input=input("Enter number to find factorial")
nums=int(get_input)
fact=1
for x in range(1,nums+1):
    fact=fact*x
print("Factorial of",nums,"=",fact)

#while loop

i=1
while i< 6:
    print("i is less than",i)
    i+=1
else:
    print("I greater than 6")
def factorial(num):
    fact=1
    for n in range(2,num+1):
        fact=fact*n
    return fact
get_input=input("Enter number to find factorial!!!")
print("Factorial of ", get_input,"=",factorial(int(get_input)))
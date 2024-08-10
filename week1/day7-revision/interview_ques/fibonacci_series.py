
#Fibonacci Series
def findFiboSeries(num):
    f1=0
    f2=1
    print(f1)
    for x in range(2,num):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3




get_input=input("Enter number for Ficonaci series")
findFiboSeries(int(get_input))

#Optimise approach
def fibonacci(n):
    fibo_series=[0,1]
    for i in range(2,n):
        fibo_series.append(fibo_series[-1]+fibo_series[-2])
    return fibo_series[:n]
num=10
print("Fibo Series=",fibonacci(num))

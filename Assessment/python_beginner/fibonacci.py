num=int(input("Enter a number"))

def fibo(n):
    fibo_series=[0,1]
    for x in range(2,n):
        fibo_series.append(fibo_series[-1]+fibo_series[-2])
    return fibo_series[:n]

print(fibo(num))
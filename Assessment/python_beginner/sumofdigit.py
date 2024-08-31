num=input("Enter number")
def sumofdigit(n):
    sum=0
    for x in range(0,len(n)):
        sum=sum+int(n[x])
    return sum
print(sumofdigit(num))

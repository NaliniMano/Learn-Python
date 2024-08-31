num=int(input("Enter a number= "))

def isPrime(num):
    for i in range(2,int(num * 0.5)+1):
               if num % i==0:
                     return False
    return True
if isPrime(num):
    print("Prime")
else:
    print("Not Prime")



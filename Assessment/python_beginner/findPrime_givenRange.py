def isPrime(num):
    for x in range(2,int(num*0.5)+1):
        if num % x ==0:
            return False
    return True
prime=[]
getinput=int(input("Enter the range to find primenumber"))
for n in range(2,getinput):
    if isPrime(n):
        prime.append(n)
print(prime)

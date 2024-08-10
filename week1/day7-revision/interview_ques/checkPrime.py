def isPrime(num):
    for n in range(2,int(num/2)+1):
        if num % n == 0:
            return False
    return True
get_input=input("Enter a number: ")
if isPrime(int(get_input)):
    print("Its prime")
else:
    print("Not prime")

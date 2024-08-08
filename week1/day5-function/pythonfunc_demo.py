def display():
    print("Function with no arguments")
def add(num1,num2):
    print(num1+num2)
display()
add(5,10)

def findAverage(*nums):
    sum=0;
    for num in nums:
        sum+=num
    avg=float(sum/len(nums))
    print("Average=",avg)
findAverage(10,15,9,12,7)

def factorial(nums):
    result=1
    for x in range(1,nums+1):
        result*=x
    return result

output=factorial(5)
print("Factorial =",output)

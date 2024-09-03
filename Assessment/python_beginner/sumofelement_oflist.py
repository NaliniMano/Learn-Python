list1=[1,2,3,4,3,1,34,-5]
def findSum(list1):
    sum=0
    for x in list1:
         sum=sum+x
    return sum

print(findSum(list1))

print(sum(list1))
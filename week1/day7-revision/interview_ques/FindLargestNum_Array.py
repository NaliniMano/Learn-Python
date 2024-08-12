def findMaxnum(arr):
    print("max num=",max(arr))
    print("min num=",min(arr))
    return sorted(arr)
number=[10,20,30,40,-10,-90,90,20]
findMaxnum(number)

print("Sorted",findMaxnum(number))
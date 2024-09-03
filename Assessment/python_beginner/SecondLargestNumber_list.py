list1=[3,5,2,1,9,10,-2,78]
list1.sort()
print(list1[-2])

# second approach
# find first max element & remove it from list1 and then again find max element from list

max_element=max(list1)
while max_element in list1:
    list1.remove(max_element)

print("Second max",max(list1))
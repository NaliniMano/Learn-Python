def armstrong_num(n):
    orginalnum=n
    add=0
    getlen=len(str(n))
    ##153 is an Armstrong number  ->1 ***3 + 5 ***3 + 3***3 =153
    ##9474 Armstrong number ->9***4+4****4+7****4+4****4 =9474
    for digit in str(n):
            n=int(digit)
            add+=n**getlen
    if orginalnum == add:
             return True
    return False

if armstrong_num(9474):
    print("Yes Armstrong")

###Optimise way
def isArmstrong(num):
    digit=[int(d) for d in str(num)]
    return num == sum(int(n)**len(digit) for n in digit)
if isArmstrong(153):
    print("ArmStrong!!!!!")
else:
    print("Not Armstrong")
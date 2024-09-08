getinput=int(input("Enter a number "))

def isEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

isEven(getinput)
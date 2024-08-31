getinput=input("Enter a word = ")
if getinput == getinput[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

def reverse_string(str):
    print(str[::-1])

reverse_string(getinput)

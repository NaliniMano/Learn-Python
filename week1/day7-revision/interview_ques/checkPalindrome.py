#Check given string palindrome
def isPalindrome(getstring):
    if getstring == getstring[::-1]:
        return True
    return False

input_str=input("Enter a String")
if isPalindrome(input_str):
    print("Its Palindrome!")
else:
    print("Not Palindrome")




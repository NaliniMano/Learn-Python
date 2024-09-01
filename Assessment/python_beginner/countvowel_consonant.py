getinput=input("Enter string: ")

def isVowel(str):
    vowellist=['a','e','i','o','u','A','E','I','O','U']
    if str in vowellist:
        return True
    return False

vowelcount=0
consonantcount=0
for x in getinput:
    if isVowel(x):
        vowelcount=vowelcount+1
    else:
        consonantcount=consonantcount+1
print("Vowel count= " , vowelcount ,"Consonant Count =",consonantcount)

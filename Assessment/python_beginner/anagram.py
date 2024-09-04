getinput1=input("Enter a word ")
getinput2=input("Enter another word ")

def fill_dict(str):
    dict1={}
    for x in str:
        dict1[x]=dict1.get(x,0)+1
    return dict1

dict1=fill_dict(getinput1)
dict2=fill_dict(getinput2)

if dict1 == dict2:
    print("Anagram")
else:
    print("Not Anagram")







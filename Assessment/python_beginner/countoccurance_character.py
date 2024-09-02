def countoccurance(str):
    dict={}
    for char in str:
        if char in dict:
            dict[char]=dict.get(char)+1
        else:
           dict[char]=1
    return dict

print(countoccurance("hhh ddd"))




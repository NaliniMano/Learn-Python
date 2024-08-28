thisdist={
    "name":"Ram",
    "age":45,
    "bloodgrop":"B+ve",
    "name":"jamy"
}

for x in thisdist:
    print(x) # default  return keys of dict

for y in thisdist.values():
    print("Values of Dict ",y) # print only values

for x in thisdist.keys():
    print("Keys of Dict ,",x)

for x,y in thisdist.items():
    print("keys=",x,"Values=",y) # print key & values


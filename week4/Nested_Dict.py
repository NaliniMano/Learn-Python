myfamily={
    "child1" : {
             "name":"mable",
              "age":2
                },
    "child2" : {
        "name":"Raki",
        "age":9
    },
    "child3" : {
        "name":"Nivi",
        "age":15
    }
}
# print particular key

print(myfamily["child1"]["age"])
for x,obj in myfamily.items():
    print("Chiled",x)
    for y in obj:
        print("Inner child",y)
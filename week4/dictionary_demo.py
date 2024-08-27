#Dictionaries are used to store data values in key:value pairs.

thisdist={
    "name":"Ram",
    "age":45,
    "bloodgrop":"B+ve",
    "name":"jamy"
}
print(thisdist)
print(thisdist["age"])
print(len(thisdist))
print(type(thisdist))

dist2=dict(name="John",age=34,blood="O+ve")
print(dist2)
print(dist2.get("name"))
get_keys=dist2.keys() # get all keys
print("Keys",get_keys)
dist2["age"]=20
print("Updated Dict",dist2)
get_values=dist2.values()  # get all values
print(get_values)

#Check if Key Exists
if "age" in dist2:
    print("Age present in Dict")
    
#  remove element from dict using key
dist2.pop("age")
print(dist2)
dist2["age"]=40
print("Added new item",dist2)
dist2.popitem()
print("Removed Last added item using pop item method",dist2)
del dist2["name"]
print("Deleted item using del",dist2)
dist3=dist2.copy()
dist2.clear()
print("Clear Dict using clear",dist2)
print(dist3)

    
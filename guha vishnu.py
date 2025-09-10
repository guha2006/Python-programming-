l={"sno":123, "name":"pappu"}
print(l)
print(l["sno"])
print(l["name"])
l["Ename"]="xyz"
print(l)
l["age"]=19
print(l)
for key in l:
    print(key)
for value in l.values():
    print(value)
for key,value in l.items():
    print(key,":",value) 
l.pop("Ename")
print(l)
l.popitem()
print(l)
l.clear()
print(l)


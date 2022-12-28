list = [{"name": "a"}, {"name": "b"}, {"name": "c"}]

for a in list:
    if a["name"] == "a":
        list.remove(a)
print(list)
        

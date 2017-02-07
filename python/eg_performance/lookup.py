from eg_decorator_TimeMe import TimeMe

# Generate fake data
a = [{ "id" : "a", "salary" : 123 }, { "id":"b" , "salary" : 456}]
b = [{ "id" : "a" , "name" :"Andy"}, { "id":"b" , "name": "Bob" }]

for i in range(1000) :
    a.append({"id" : i , "salary" : i *10})
    b.append({"id" : i , "name" : i *100})

### Start ###

@TimeMe("method 1")
def method1(a, b) :
    for i in a :
        for j in b :
            if(i["id"] == j["id"]):
                i["name"] = j["name"]
    return a

method1(a, b)

@TimeMe("method 2")
def method2(a, b) :
    lookup = {}
    for i in b :
        lookup[i["id"]] = i["name"]

    for i in a :
        i["name"] = lookup.get(i["id"])
    return a

method2(a, b)




# Intern interview questions

# Any problems with this code?
# How to fix.
box = [
    { "id" : 1},
    { "id" : 2}
]

tmp = []
for b in box :
   if("items" not in b ) :
       b["items"] = tmp

box[0]["items"].append("apple")
box[1]["items"].append("orange")

for b in box :
    print(b["id"] ,  b["items"])

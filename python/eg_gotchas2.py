import time
r = list(range(3))
print(r)

k = ["a", "b", "c", "d", "e"]
i=0
for c in r :
    print("c={0}  i={1} k[i]={2}".format(c,i,k[i]))
    r.append(k[i])
    i = i +1
    print(c)
    time.sleep(5)


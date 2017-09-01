

def somefunc(a=[]) :
    a.append('orange')
    return a

print(somefunc())

print(somefunc(a=["apple "]))

print(somefunc())

print(somefunc(a=["apple "]))


# Another example with class
class T() :
    def __init__(self, ar=[], d={}):
        self.a = ar
        self.d = d


t1 = T()
t1.a.append("one")
t1.d["x"] = "xxxx"

t2 = T()
t2.a.append("two")
t1.d["y"] = "yyyy"

print(t1.a)
print(t2.a)

print(t1.d)
print(t2.d)

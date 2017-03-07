
# List
list = [ x * 2 for x in range(3)]
print(list)

# Generator
generator = (x * 2 for x in range(3))
print(generator)
for i in generator : print(i) # this is iterates but
for i in generator : print(i) # this wont' iterate again as generator loops only once

# Yield
def doSomething(i) :
    print("Doing something", i)

def createGen() :
    print("Start createGen")
    for i in range(3) :
        doSomething(i)
        yield "x"

mygen = createGen()

for i in (mygen) :
    pass


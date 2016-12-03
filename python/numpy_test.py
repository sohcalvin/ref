import numpy as np
def printIt(label, obj) :
    print("\nNote that " +label +" :\n" + str(obj) + "\nis of type " + str(type(obj)))

def printIt2(label, obj) :
    print(label +" :\n" + str(obj))

dict = {"cat": 1, "dog": 2}
dict["a"] = 1
dict["b"] =2
printIt("#Demo dictionary",dict)


print("\n# Demo numpy array properties\n------------------------------------")
arr1 = np.array([[15,28,2],[12,25,22],[17,29,5]])
print("type = " + str(type(arr1)));
print("The datax : \n" + str(arr1))
print("ndim = " + str(arr1.ndim));
print("size = " + str(arr1.size));
print("nbytes = " + str(arr1.nbytes));

print("\n# Demo Matrix multiplication\n------------------------------------")
cost = np.array([1,2,3]) # drink, muffin, cake
partyOrder = np.array([[15,28],[12,25],[17,29]])

totalByParty = cost.dot(partyOrder)

print('cost :\n' + str(cost))
print('partyOrder :\n' + str(partyOrder))

print('totalByParty :')
print(totalByParty)

print("\n# Demo mean, std, min, max\n------------------------------------")
array = np.array([2,3,10])
print("mean of " + str(array) + " is " + str(array.mean()))
print("std  of " + str(array) + " is " + str(array.std()))
print("min  of " + str(array) + " is " + str(array.min()))
print("max  of " + str(array) + " is " + str(array.max()))

print("median  of " + str(array) + " is " + str(np.median(array)))
print("25th percentile of " + str(array) + " is " + str(np.percentile(array,25)))

print("\n# Demo arange\n------------------------------------")
array2 = np.arange(start=3,stop=12,step=2)
print(array2)

print("\n# Demo split\n------------------------------------")
array3 = np.arange(15)
alist = np.split(array3,3)
array31 = np.array(alist)
print("Note that list :\n" + str(alist) + "\nis of type " + str(type(alist)))
print("\nNote that array31 :\n" + str(array31) + "\nis of type " + str(type(array31)))

array3.size
print("\n# Demo random\n------------------------------------")
randomData = np.random.rand(2,3)
print("Note that randomData :\n" + str(randomData) + "\nis of type " + str(type(randomData)))

print("\n# List comprehension\n------------------------------------")
arr4 = [1,2,3]
print(arr4)

squaredX= [ x**2 for x in arr4]
print(squaredX)

squaredXFiltered= [ x**2 for x in arr4 if x%2==0]
print(squaredXFiltered)

y = [z for x in range(1, 3) for z in range(x*2,6)]
print(y)

print("\n# Regexp\n------------------------------------")
import re
my_regex = re.compile("[0-9]+", re.I)

print("\n# Demo lambda\n------------------------------------")
def applyFunc(f,arg1, arg2) :
    return f(arg1, arg2)
result = applyFunc(lambda x, y : x + y , 3, 5)
print(result)

print("\n# Demo function default arg, named arg\n------------------------------------")
def my_print(message="my default message"):
    print(message)
my_print()

def subtract(a=0, b=0):
    return a - b
subtract(10, 5) # returns 5
subtract(0, 5) # returns -5
subtract(b=5) # returns -5

print("\n# Demo string\n------------------------------------")
print("Length of 'abc' is " +  str(len("abc")))

print("Raw string " + r"\t")
print("Single quote for slash tab not raw string " + '\t')

print("""Tripple quote for mulitline
one
two
three""")

print("\n# Demo try except\n------------------------------------")
try:
    print(0/0)
except ZeroDivisionError :
    print("Cannot divide by zero - " + str(ZeroDivisionError))

print("\n# Demo List\n------------------------------------")
print("List is like an array that can have different datax type")
integerList = [1,2,3]
integerList2 = [4,5,6]
heterogeneousList = ["String", 0.1, True]
integerList.extend(integerList2)
comboList = integerList + heterogeneousList

print(len(integerList))
print(sum(integerList))
print(integerList)
print(comboList)
comboList.append("lastrec")
print(comboList)

print("\n# Demo Range\n------------------------------------")
def printRange(r):
    print(list(r))



x = range(10) # starts from zero
printRange(x)
print(x[4])
print(x[-1]) # equals 9

first_three = x[:3]
printRange(first_three)

three_to_end = x[3:]
printRange(three_to_end)

one_to_four = x[1:5] # [1, 2, 3, 4]

last_three = x[-3:] # [7, 8, 9]
printRange(last_three)

without_first_and_last = x[1:-1] # [1, 2, ..., 8]
printRange(without_first_and_last)

copy_of_x = x[:] # [0, 1, 2, ..., 9]
printRange(copy_of_x)

print("\n# Demo Dictionary\n------------------------------------")
print("""
Dictionary keys must be immutable; in particular, you cannot use lists as keys. If
you need a multipart key, you should use a tuple or figure out a way to turn the key
into a string.
""")

adict = {"a" : "apple", "b" : "banana"}
print("adict = "+ str(adict))
print("adict['a'] = "+ str(adict['a']))

bExist = "b" in adict
print("\"b\" in adict is "+ str(bExist))

print("adict.get(\"a\") is " + adict.get("a"))
print("adict.get(\"xx\") is " + str(adict.get("xx") ))

for i in (adict.items()) :
    print(i)


print("\n# Demo Default Dictionary : defaultdict\n------------------------------------")
print("""
These will be useful when we’re using dictionaries to “collect” results by some key and
don’t want to have to check every time to see if the key exists yet.
""")
from collections import defaultdict

aDefaultDict = defaultdict(int) # int is a function which returns zero with no arg
aDefaultDict["a"] += 2
print(aDefaultDict)

aDefaultDict = defaultdict(lambda : 3) # lambda return 3 which is the init value
aDefaultDict["b"] += 2
print(aDefaultDict)

print("\n# Demo Counter\n------------------------------------")
from collections import Counter
c = Counter(["red","blue","red","green","green","yellow"])
print(c)
print(c.most_common(2)) # print top 2 highest count words

print("\n# Demo Set\n------------------------------------")
s= set()
s.add("red")
s.add("blue")
s.add("red")
print(len(s))
print(s)

print("""
Apart from using Set as a distict collection,
Set operation is fast,
So comparing
x in list
 and
x in set   <<--- this is much faster

You can convert list to set by passing list as an arg to set(alist)
""")
l = ["red","red", "red"]
s2 = set(l)
print(s2)

print("\n# Demo Truthiness\n------------------------------------")
x = None
print(x == None) # prints True, but is not Pythonic
print(x is None) # prints True, and is Pythonic

print(all([1,"red",True]))
print(all([1,"red",True, None]))
print(any([1,"red",True, None]))


print("\n# Demo Sort\n------------------------------------")
print("""Sort in place
------------------ """)

alist = [ -5,3,9]
printIt2("Before sort " , alist)
alist.sort()
printIt2("After sort " , alist)
alist.sort(reverse=True)
printIt2("After sort reverse" , alist)
alist.sort(key=abs, reverse=True)
printIt2("After sort reverse by abs function" , alist)

print("""Sort return new list
------------------ """)
newList = sorted(alist)
printIt2("New list sort" , newList)

print("\n# Demo Lazy range\n------------------------------------")
print("""
(Python actually comes with a lazy_range function called xrange, and in Python 3,
range itself is lazy.) This means you could even create an infinite sequence:
""")

arange =  range(3)
for i in arange :   print(i)
for i in arange :   print(i)


print("\n# Demo map\n------------------------------------")
a  = [1,2]
b  = [3,4]
c = map(lambda x,y : x*y, a, b)
for i in (c) :
    print(i)

print("\n# Demo enumerate\n------------------------------------")
data = { "a" : "apple" , "b" : "banana"}
for i, k in enumerate(data):
    print(str(i) +  ">" +  str(k))

keys= list(data.keys())
print("\nfor array = " + str(keys))
for i, k in enumerate(keys):
    print(str(i) +  ">" +  str(k))

print("\n# Demo zip\n------------------------------------")
def demo_zip() :
    x = [1,2,3]
    y = [4,5,6]
    z = zip(x,y)
    zarray = [ a for a in z]
    print(zarray)
demo_zip()
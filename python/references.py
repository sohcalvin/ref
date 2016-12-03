
# If else
if True :
    print("It's true")
elif False :
    print("It's false")
else :
    print("It's also false")

# File operation
filename="t.txt"

print("Opening " + filename + " for write")
fileHandle = open(filename, "w")
fileHandle.writelines("line one\n")
fileHandle.writelines("line two")
fileHandle.close()
print("Writing " + filename + " done")

print("\n")
print("Opening " + filename + " for read")
fileHandle = open(filename, "r")
fileContents=fileHandle.read()
fileHandle.close()
print("File contents\n--------\n" + fileContents + "\n----------")

# Array
anArray =  [1,2,3]

# Triple quotes
def demoTripleQuotes() :
    aLongSentence = """Hello how
    are you
    today """
    print (aLongSentence)
demoTripleQuotes()

def demoString(aString) :
    print("\nString operation\n")
    print("Index of '23' in " + aString + " is " + str(aString.find("23")))
    print(aString[4:6])
demoString("0123456789")
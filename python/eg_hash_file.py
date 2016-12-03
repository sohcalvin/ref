import hashlib




def hashBytes(bytes) :
    hasher = hashlib.sha1()
    hasher.update(bytes)
    return hasher.hexdigest()


print(hashBytes(b'asdf'))
print(hashBytes(b'''
asdfasdfsa

asdfas
dfa
sdf
asd
fas
dfa
sdf
asd
f

'''))

#
#
# with open('anotherfile.txt', 'rb') as afile:
#     buf = afile.read(BLOCKSIZE)
#     while len(buf) > 0:
#         hasher.update(buf)
#         buf = afile.read(BLOCKSIZE)
# print(hasher.hexdigest())
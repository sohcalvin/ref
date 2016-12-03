from pymongo import MongoClient
import gridfs

db = MongoClient().gridfs_example
fs = gridfs.GridFS(db)

pdfFile = open("C:/tmp/Developer_CV.pdf", "rb")

content = pdfFile.read()
pdfFile.seek(0)
stored_id = fs.put(pdfFile, filename="foo", bar="baz")
out = fs.get(stored_id)

print('''
File saved.
filename was {0}
bar was {1}
upload_date as {2}
'''.format(out.filename, out.bar, out.upload_date))

newfile = open("c:/tmp/qq3.pdf", "wb")
newfile.write(out.read())



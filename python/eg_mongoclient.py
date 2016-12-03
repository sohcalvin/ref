from pymongo import MongoClient, TEXT
import gridfs

db = MongoClient("127.0.0.1", 27017, maxPoolSize=1, connect=False)["somedb"]

db.cv.create_index([("raw_content", TEXT)])
db.job.create_index([("title", TEXT), ("description_cleaned", TEXT)])
db.rec_cache.create_index("createdAt", expireAfterSeconds=10*60)
fs = gridfs.GridFS(db)
id = db.job.insert({"active" : True})
s=True
for i in range(1, 100000) :
    x = db.job.find()
    for k in x :

        s = not s
        db.job.update(
            {"_id" : id},
            {
                "$set" : {"active" :  s}
            }
        )

        print(i)

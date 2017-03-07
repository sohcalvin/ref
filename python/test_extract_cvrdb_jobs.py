from pymongo import MongoClient, TEXT
import gridfs
from bson.objectid import ObjectId


db = MongoClient("127.0.0.1", 27017, maxPoolSize=1, connect=False)["cvr_db"]

jobs = db.job.find({"owner" : "api8.successfactors.com"})

extracted = {}
i=1;
for job in jobs :
   if(i >1) : break
   job_id = str(job["_id"])
   cv_applied = job["cv_applied"]
   if(cv_applied is None or len(cv_applied) == 0) :
     continue
   extracted[job_id] = {
      "job_description" : job["description_cleaned"],
      "job_title" : job["title"]
   }
   cv_info = {}
   #if(cv_applied is not None and len(cv_applied) > 0) :
   for cv_id, v in cv_applied.items() :  	
         cv_job_application_status = v.get("job_application_status")
         cv = db.cv.find_one({"_id" : ObjectId(cv_id)})
         cv_raw_content = cv["raw_content"]
         cv_info[cv_id] ={
		"cv_id" : cv_id,
		"job_application_status" : cv_job_application_status,
		"cv_raw_content" : cv_raw_content
         }
   extracted[job_id]["cv_applied"] = cv_info
   i += 1
import json

extracted_json= json.dumps(extracted,indent=4, ensure_ascii=False).encode('ascii', 'ignore').decode("ascii")
#print(extracted_json)
out = open("t.txt", "w")
out.write(extracted_json)

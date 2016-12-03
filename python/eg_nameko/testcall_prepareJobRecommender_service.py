# from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy
import base64

CONFIG = {'AMQP_URI': "amqp://localhost:5672"}

jobs =\
    [
        {
            "_id": "111",
            "description" : "Job1 description, one two three four five"

        },
        {
            "_id": "222",
            "description": "Job2 description, one two three four five"
        }
    ]

import os
os.environ["https_proxy"] = "http://proxy.sin.sap.corp:8080"
def prepareJobRecommender(jobs_list) :
    # pdfFile = open("sample.pdf", "rb")
    # pdfbytes = pdfFile.read()
    with ClusterRpcProxy(CONFIG) as rpc:
        # base64_encoded_bytes = base64.b64encode(pdfbytes)
        # base64_encoded_str = base64_encoded_bytes.decode("utf-8")
        result = rpc.job_matcher.prepareJobRecommender(jobs_list, "xxcsohtenanat")
    return result

def getJobRecommender() :
    # pdfFile = open("sample.pdf", "rb")
    # pdfbytes = pdfFile.read()
    with ClusterRpcProxy(CONFIG) as rpc:
        # base64_encoded_bytes = base64.b64encode(pdfbytes)
        # base64_encoded_str = base64_encoded_bytes.decode("utf-8")
        result = rpc.job_matcher.job_matching_to_cv("Java spring hibernate", "xxcsohtenanat")
    return result


# from cvrml.app.crawlers.sap_jobs.sap_jobs_feeder import getSapJobsFromURLFeeds
# jobs = getSapJobsFromURLFeeds("https://jobsearch.createyourowncareer.com/feed/177801")
# print(jobs)



#
# from cvr.service.job_service import JobService
# js = JobService()
# jobs = js.getAllJobsByCurrentUser("jobs.sap.com")
# job_list = [ j.to_dict(['_id', 'description']) for j in jobs]
# prepareJobRecommender(job_list)


#
print(getJobRecommender())



from flask import Flask, request
from flask_security import login_required, http_auth_required, roles_required
import io
import os
import subprocess
import json
from pymongo import MongoClient
from cloudfoundry_util import getMongodbUriFromCloudfoundryEnv
from security_imports import configureSecurityMongoDb, ADMIN_ROLE, makeMongodbUri
import pika
from cvr_db import CvrDb


app = Flask(__name__)

#### Get Backing service URIs ####
dbname2uri_map = getMongodbUriFromCloudfoundryEnv()
USERDB_URI = dbname2uri_map.get("admin-mongodb")
CVRDB_URI = dbname2uri_map.get("cvr-mongodb")
RABBITMQ_URI = getMongodbUriFromCloudfoundryEnv().get("cv-rabbitmq")
RABBITMQ_QUEUES = ["rpc-job_matcher", "rpc-career_level_classifier"]

if(USERDB_URI is None or CVRDB_URI is None or RABBITMQ_URI is None) :
    print("Running in Local enviroment due to cloudfoundry mongodb not found in VCAP_SERVICES environment")
    USERDB_URI =  makeMongodbUri("user_db")
    CVRDB_URI = makeMongodbUri("cvr_db")
    RABBITMQ_URI =  'amqp://guest:guest@localhost:5672/'
else :
    print("Running in Cloud Foundry enviroment")


### Declaration and Setup
configureSecurityMongoDb(app, user_mongodb_uri=USERDB_URI)
cvr_db = db1 = MongoClient(CVRDB_URI).get_default_database()

pika_conn_params = pika.URLParameters(RABBITMQ_URI)
rabbitmq_connection = pika.BlockingConnection(pika_conn_params)

cvr_db_obj = CvrDb(cvr_db)



@app.route('/mongo', methods = ['POST', 'GET'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def mongo():
    import sys
    cmd1 = request.args.get("cmd")
    cmd2 = request.form.get("cmd")
    cmd3 = request.data
    if(cmd3) :
        cmd =cmd3
    elif(cmd2) :
        cmd =cmd2
    else :
        cmd =cmd1
    cmd = cmd.decode("ascii")
    buffer = io.StringIO()
    sys.stdout = buffer
    exec(cmd)
    return "{0}".format(buffer.getvalue()), 200

@app.route('/cvr/adduser', methods = ['POST'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def cvrAddUser():
    user_data = {
        "email": ["test_user1@comcast.com"],
        "first_name": ["test"],
        "last_name": ["user1"],
        "password": "1234512345",
        "organization": 'api8.successfactors.com',
        "tenant": "comcast",
        "roles": ["recruiters"]
    }
    cvr_db.user.insert(user_data)









{
    "id": "ten1",
    "title": "Tenant1",
    "header_labels": ["Property", "Value"],
    "header_keys": ["property", "value"],
    "data": [
        {
            "property": "Job count",
            "value": "10"
        },
        {
            "property": "CV count",
            "value": "30"
        }
    ]

}

@app.route('/summary', methods = ['GET'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def summary():
    data = cvr_db_obj.getSummary()

    jobs_cnt = db1.job.find().count()
    cv_cnt = db1.cv.find().count()
    distinct_owner = db1.job.distinct("owner")
    distinct_organization = db1.job.distinct("organization")
    b = "<br>"
    resp = "Total jobs : {}{}".format(jobs_cnt, b)
    resp +=  "Total cvs : {}{}".format(cv_cnt, b)
    resp += b

    resp += "<b>Distinct owners :</b> {}".format(b)
    for o in distinct_owner :
        resp += "- {}{}".format(o, b)
    resp += b

    resp += "<b>For each organization :</b> {}".format(b)
    resp += "<hr>"
    for o in distinct_organization:
        resp += "<table>"
        resp += "<tr><td>{}</td> <td>{}</td></tr>".format("Organization", o)
        resp += "<tr><td>{}</td> <td>{}</td></tr>".format("Jobs", db1.job.find({"organization" : o }).count())
        resp += "<tr><td>{}</td> <td>{}</td></tr>".format("Jobs - active",db1.job.find({"organization": o, "active" : True }).count() )
        resp += "<tr><td>{}</td> <td>{}</td></tr>".format("Jobs - active with cvs", db1.job.find(
            {"organization": o, "active": True, 'cv_ids': {'$exists': True, '$ne': []}}).count())

        resp += "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td></tr>"
        resp += "</table>"
        resp += "<hr>"
    resp += b

    for qn in RABBITMQ_QUEUES:
        channel = rabbitmq_connection.channel()
        queue = channel.queue_declare(
            queue=qn, durable=True,
            exclusive=False, auto_delete=False
        )
        print("{} : {}".format(qn, queue.method.message_count))

    return "<html>{}</html>".format(resp), 200







if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


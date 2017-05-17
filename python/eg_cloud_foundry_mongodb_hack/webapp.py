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
from util_rabbitmq import getRabbitmqQueues
from util_formatter import formatListDict2HtmlTable

app = Flask(__name__)

#### Get Backing service URIs ####
dbname2uri_map = getMongodbUriFromCloudfoundryEnv()
USERDB_URI = dbname2uri_map.get("admin-mongodb")
CVRDB_URI = dbname2uri_map.get("cvr-mongodb")
RABBITMQ_URI = getMongodbUriFromCloudfoundryEnv().get("cv-rabbitmq")
RABBITMQ_QUEUES = [
"rpc-career_level_classifier",
"rpc-cv_content_classifier",
"rpc-cv_parsing_service",
"rpc-date_extractor_service",
"rpc-document_matcher_service",
"rpc-industry_classifier",
"rpc-job_matcher",
"rpc-job_title_extractor",
"rpc-keyword_generator_service",
"rpc-location_extractor"
        ]

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



############ API ############

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

@app.route('/summary', methods = ['GET'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def summary():
    distinct_data = cvr_db_obj.getDistinctSummary()
    data = cvr_db_obj.getSummary()
    queues = getRabbitmqQueues(rabbitmq_connection, RABBITMQ_QUEUES)
    if(request.args.get("format") == "json") :
        return json.dumps({
            "distinct_data" : distinct_data,
            "data" : data,
            "queues" : queues
        }), 200
    else :
        distinct_data_html = formatListDict2HtmlTable(["owner", "organization"], distinct_data)
        data_html = formatListDict2HtmlTable(["owner", "cv_count", "job_count", "job_count_active", "job_count_active_with_cvs"], data)
        queues_html = formatListDict2HtmlTable(["queue", "message_count"], queues)
        return "{}<br>{}<br>{}".format(distinct_data_html, data_html, queues_html) , 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


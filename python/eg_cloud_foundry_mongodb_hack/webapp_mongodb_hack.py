from flask import Flask, request
from flask_security import login_required, http_auth_required, roles_required
import io
import os
import subprocess
import json
from pymongo import MongoClient
from cloudfoundry_util import getMongodbUriFromCloudfoundryEnv
from security_imports import configureSecurityMongoDb, DEFAULT_MONGODB_URI, ADMIN_ROLE, makeMongodbUri

app = Flask(__name__)

dbname2uri_map = getMongodbUriFromCloudfoundryEnv()
USERDB_URI = dbname2uri_map.get("admin-mongodb")
CVRDB_URI = dbname2uri_map.get("cvr-mongodb")

if(USERDB_URI is None or CVRDB_URI is None) :
    print("Running in Local enviroment due to cloudfoundry mongodb not found in VCAP_SERVICES environment")
    USERDB_URI = None
    CVRDB_URI = makeMongodbUri("cvr_db")
else :
    print("Running in Cloud Foundry enviroment")

configureSecurityMongoDb(app, user_mongodb_uri=USERDB_URI)
db1 = MongoClient(CVRDB_URI).get_default_database()

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

@app.route('/summary', methods = ['GET'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def summary():
    import sys
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
    return "<html>{}</html>".format(resp), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


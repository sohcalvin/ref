from flask import Flask, request
from flask_security import login_required, http_auth_required, roles_required
import os
import io
import subprocess

from pymongo import MongoClient
import json
app = Flask(__name__)

from security_imports import configureSecurityMongoDb, DEFAULT_MONGODB_URI, ADMIN_ROLE, makeMongodbUri

def getMongodbListUriFromCloudfoundryEnv() :
    env_config = os.environ.get('VCAP_SERVICES')
    mongodb_uri = []
    if env_config:
        vcapJsonObj = json.loads(env_config)

        for c in [ 'mongodb', 'user-provided'] :
            if(c in vcapJsonObj):
                config_list = vcapJsonObj[c]
                for i in config_list :
                    uri = i['credentials']['uri']
                    mongodb_uri.append(uri)
                    # mongodb_clients.append(MongoClient(uri).get_default_database())
                break # Only do one
    return mongodb_uri
        #
        # mongo_config = vcapJsonObj['mongodb']
        # mongodb_list = []
        # if('mongodb' in vcapJsonObj):
        #     uri = vcapJsonObj['mongodb'][0]['credentials']['uri']
        # elif('user-provided' in vcapJsonObj) :
        #     uri = vcapJsonObj['user-provided'][0]['credentials']['uri']
    # return MongoClient(uri).get_default_database()

def isCloudFoundryEnv(uri_list) :
    return True if (len(uri_list) == 2) else False

uri_list = getMongodbListUriFromCloudfoundryEnv()
if(isCloudFoundryEnv(uri_list)) :
    userdb_uri  = uri_list[0]
    cvr_uri     = uri_list[1]
else :
    userdb_uri = None
    cvr_uri = makeMongodbUri("cvr_db")

configureSecurityMongoDb(app, user_mongodb_uri=userdb_uri)

db1 = MongoClient(cvr_uri).get_default_database()

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
    cv_cnt = db1.job.find().count()
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
        resp += "<tr><td>{}</td> <td>{}</td></tr>".format("Jobs - active with cvs", db1.job.find({"organization": o, "active": True, 'cv_ids': {'$exists': True}, "$where": "this.cv_ids.length > 0"}).count())
        resp += "<tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td></tr>"
        resp += "</table>"
        resp += "<hr>"
    resp += b
    return "<html>{}</html>".format(resp), 200


if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


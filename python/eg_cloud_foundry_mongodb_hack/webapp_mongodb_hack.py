from flask import Flask, request
import os
import io

from pymongo import MongoClient
import json
app = Flask(__name__)

def getMongodbFromCloudfoundryEnv() :
    env_config = os.environ.get('VCAP_SERVICES')
    uri = None
    if env_config:
        vcapJsonObj = json.loads(env_config)
        if('mongodb' in vcapJsonObj):
            uri = vcapJsonObj['mongodb'][0]['credentials']['uri']
        elif('user-provided' in vcapJsonObj) :
            uri = vcapJsonObj['user-provided'][0]['credentials']['uri']
    return MongoClient(uri).get_default_database()

db = getMongodbFromCloudfoundryEnv()

@app.route('/mongo', methods = ['POST', 'GET'])
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


if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


from flask import Flask
import sys
from pymongo import MongoClient, TEXT
import os
app = Flask(__name__)

host=os.environ.get("MONGO_PORT_27017_TCP_ADDR")
port=int(os.environ.get("MONGO_PORT_27017_TCP_PORT"))

db= MongoClient(host,port, maxPoolSize=200)["cvr_db"]
db.xx.insert({"fruit" :"apple"})

@app.route('/')
def page1():
   print("page1")
   f = db.xx.find_one()
   return "success page1 :{0}".format(f) ,200


@app.before_request
def before_request() :
    pass

if __name__ == '__main__':
    print("Running on localhost:5001")
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)

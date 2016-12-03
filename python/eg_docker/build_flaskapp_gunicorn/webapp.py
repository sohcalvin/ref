from flask import Flask
app = Flask(__name__)
import os
import sys

import logging

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

app.logger.debug("Hello World")
pid = os.getpid()

@app.route('/')
def page1():
   app.logger.debug("Hello World : {0} ".format(pid))
   f=">>>>>>preload pid={0}-- workerpid={1}".format(pid, os.getpid())
   print(f)
   return "success page1 :{0}".format(f) ,200


@app.before_request
def before_request() :
    pass

if __name__ == '__main__':
    print("Running on localhost:5001")
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)

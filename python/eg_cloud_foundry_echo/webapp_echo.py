from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def echo():
   out="Client Address : " + request.remote_addr + "<br>"
   for r in request.headers.keys():
       out = out + "{0} : {1}<br>".format(r, request.headers[r])
   return out, 200


if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


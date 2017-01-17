from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
import os
import json
app = Flask(__name__, static_url_path='',static_folder='static')
CORS(app)
# @app.route('/')
# def root():
#     # return "adf",200
#     return app.send_static_file('domain.xml')
#
# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)

@app.route('/headers', methods = ['POST', 'GET'])
def headers():
   out="Client Address : " + request.remote_addr + "<br>"
   for r in request.headers.keys():
       out = out + "{0} : {1}<br>".format(r, request.headers[r])
   return out, 200

@app.route('/myip', methods = ['POST', 'GET'])
def myip():
    out = {"ip" : request.remote_addr}
    return json.dumps(out), 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on port {0}".format(port))
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


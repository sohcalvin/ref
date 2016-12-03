from flask import Flask, request, redirect
from werkzeug.wrappers import Response
import os
import sys
import re
import io

from pymongo import MongoClient, TEXT
import json
app = Flask(__name__)
# api = Api(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
    # return redirect("https://api.yaas.io/srp/csohtest/v1/", code=303)
    # return "home success {0}<hr> {1}<hr>{2}".format(output, os.environ, host) ,200
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Location': "https://api.yaas.io/srp/csohtest/v1/",
            'Authorization' : "Bearer 022-d539de8f-e08f-4ec6-a490-8f2148e9665f",
            'SOMEHEADER' : "HEADERVALUE"
    }

    return Response("https://api.yaas.io/srp/csohtest/v1/", status=302, headers=headers)

@app.route('/toexample')
def to_example():
    return redirect("https://api.yaas.io/srp/csohtest/v1/", code=303)


@app.after_request
def after_request(response):
    response.headers.add('Custom-Header', 'Custom Header')
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('APPLE', 'RED')
    response.set_cookie('some-cookie', value='some-cookie-value')
    return response


if __name__ == '__main__':

    # print(">>>>>>>>>>>>")
    # print(os.path.isfile(".cvr.properties"))
    # for index, each in enumerate(sorted(os.environ.items())):
    #                    print(index, each)
    #
    # # port = int(os.getenv("VCAP_APP_PORT"))
    port = int(os.getenv("PORT", 9099))

    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)
    # app.run(host='0.0.0.0' port=8080, debug=True)

from flask import Flask, request

import io
import os

app = Flask(__name__)

from urllib.request import HTTPError, urlopen, Request

import requests

USER_AGENT = 'OpenAnything/1.0 +http://diveintopython.org/'

import ssl
def getUrlContent(url):
    request = Request(url)
    request.add_header('User-Agent', USER_AGENT)
    try:
        # context = ssl._create_unverified_context()
        # response = urlopen(request, context=context)
        response = urlopen(request)
        print ("start reading")
        document = response.read().decode("utf-8", "ignore")
        print ("done reading")
        return document
    except HTTPError as e:
        print('HTTP Error {e.code}: {e}'.format(e=e))


# ss = getUrlContent("https://www.redsapsolutions.com/api/v1/feeds/276418b5-8ef8-45c9-a551-70692b52ee9e.xml")
# print(ss)
#
# import requests

def check_ssl(url):
    try:
        req = requests.get(url, verify=True)
        print(url + ' has a valid SSL certificate!')
    except requests.exceptions.SSLError:
        print(url + ' has INVALID SSL certificate!')





@app.route('/test', methods = ['POST', 'GET'])
def mongo():
    return getUrlContent("https://www.redsapsolutions.com/api/v1/feeds/276418b5-8ef8-45c9-a551-70692b52ee9e.xml") ,200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)


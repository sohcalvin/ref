from flask import Flask, redirect, request
import os
import requests
import requests.auth
app = Flask(__name__)




URL_GEN_TOKEN = "https://ml-test.apimanagement.hana.ondemand.com/mlservice_oauth/generateToken"
URL_CREATE_HASH = "https://validation-cvr-dataservice.cfapps.us10.hana.ondemand.com/cvr/create-hash"
# URL_CREATE_HASH = "https://ml-test.apimanagement.hana.ondemand.com/recommender/matchcvtojob"

URL_JOBMATCHER= "https://validation-sap-jobmatcher.cfapps.us10.hana.ondemand.com/#/"

def getAccessToken():
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "client_credentials"}
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    response = requests.post(URL_GEN_TOKEN,
							 auth=client_auth,
							 data=post_data,
                             headers= headers)
    token_json = response.json()
    # print(token_json)
    return token_json['access_token']

def getHash(access_token) :
    # payload = """{
    #         "jobDesc": "Java Programmer",
    #         "cvText": "SmF2YSBQcm9ncmFtbWVy",
    #         "keywordList": "Java, Programmer",
    #         "cvListEncoding": "Base64",
    #         "customerId": "abc",
    #         "jobId": "def",
    #         "cvId": "ghi",
    #         "jobTitle": "jkl"
    #     }"""
    payload=""
    headers = {"authorization" : "Bearer {}".format(access_token), "HTTP_API_MGMT_TOKEN" : "Bearer {}".format(access_token)}
    response = requests.post(URL_CREATE_HASH, data=payload, headers=headers)

    # token_json = response.json()
    print(response)
    return response


@app.route('/', methods = ['POST', 'GET'])
def home():
    return """
            <a href='jobmatcher'>Job Matcher</a>


    """ ,200

@app.route('/jobmatcher', methods = ['POST', 'GET'])
def redirectToJobMatcher():
    access_token = getAccessToken()
    hash= getHash(access_token)
    # return access_token , 200
    return redirect(URL_JOBMATCHER + str(hash), code=302)

@app.route('/abc', methods = ['POST', 'GET'])
def abc() :
    BEARER_STR = 'Bearer'
    api_mgmt_token = None
    for i in request.headers.environ :
        print(i + "==" )

    for i in request.headers :
        print(i  )

    if 'HTTP_API_MGMT_TOKEN' in request.headers.environ \
            and request.headers.environ['HTTP_API_MGMT_TOKEN'] is not None \
            and len(str(request.headers.environ['HTTP_API_MGMT_TOKEN']).strip()) > 0:
        api_mgmt_token = str(request.headers.environ['HTTP_API_MGMT_TOKEN']).replace(BEARER_STR, '').strip()

    return "asdf", 200

if __name__ == '__main__':
    port = int(os.getenv("PORT", 9099))
    print("Running on")
    app.run(host='0.0.0.0', debug=True, port=port, threaded=True)

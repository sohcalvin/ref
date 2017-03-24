from flask import Flask, request
from flask_restful import Api
from flask_security import Security,current_user, http_auth_required, roles_required
app = Flask(__name__)
api = Api(app)

from security_imports import configureSecurityMongoDb, ADMIN_ROLE
configureSecurityMongoDb(app)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return "home success ",200

@app.route('/page1', methods = ['POST', 'GET'])
@http_auth_required
@roles_required(ADMIN_ROLE)
def page1():
    return "success page1 by admin role" + current_user.email,200

@app.route('/page2', methods = ['POST', 'GET'])
@http_auth_required
def page2():
    print("page2")
    cu = current_user.email
    return "success page2" + cu,200

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Authentication-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    # # Adjust these headers accordingly
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
    # # X-Requested-With, Content-Type, Accept"
    # response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # response.headers.add('Access-Control-Expose-Headers','*')
    #
    # response.headers.add('Access-Control-Allow-Credentials','true')
      # Context.Response.AddHeader("Access-Control-Allow-Origin", Context.Request.Headers["Origin"]);
      #           Context.Response.AddHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
      #           Context.Response.AddHeader("Access-Control-Allow-Methods", "GET, POST PUT, DELETE, OPTIONS");
      #           Context.Response.AddHeader("Access-Control-Allow-Credentials", "true");
    return response

if __name__ == '__main__':
    print("Running on localhost:5001")
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)
    # app.run(host='0.0.0.0' port=8080, debug=True)

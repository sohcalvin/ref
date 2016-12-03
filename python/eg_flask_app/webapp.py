from flask import Flask
from flask_restful import Api
import sys

app = Flask(__name__)
api = Api(app)

########################33
#############################
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required, auth_token_required, current_user,logout_user
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = False
# app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = 'saltit'
# app.config['WTF_CSRF_ENABLED'] = False
# app.config['SECURITY_LOGIN_URL'] = '/testlogin'
# MongoDB Config
app.config['MONGODB_DB'] = 'cvr_db'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
db = MongoEngine(app)

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    name = db.StringField(max_length=255)
    email = db.StringField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])
    job_ids = db.ListField()


# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)
#############################
@app.route('/', methods = ['POST', 'GET'])
def home():

    return "home success " + current_user.email,200

@app.route('/page1', methods = ['POST', 'GET'])
# @login_required
@auth_token_required
def page1():
    print("page1")
    return "success page1" + current_user.email,200

@app.route('/page2', methods = ['POST', 'GET'])
# @login_required
@auth_token_required
def page2():
    print("page2")
    cu = current_user.email
    # logout_user()
    # try :
    #     print(">>>" , current_user.get_auth_token())
    # except:
    #     print( sys.exc_info())
    return "success page2" + cu,200


@app.before_request
def before_request() :
    pass

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

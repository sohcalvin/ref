from flask import request
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, utils, roles_accepted, roles_required, http_auth_required, current_user, login_required
ADMIN_ROLE = "admin"

DEFAULT_MONGODB_URI = "mongodb://localhost:27017/user_db"


def makeMongodbUri(db_name, server="localhost", port ="27017"):
    return "mongodb://{}:{}/{}".format(server, port, db_name)

def initAdminUser(user_datastore) :
    role = user_datastore.find_role(ADMIN_ROLE)
    if(role is None) :
        print("Initializing admin role")
        user_datastore.create_role(name=ADMIN_ROLE, description="Administrator")
    admin_email = "su@admin.com"
    user = user_datastore.find_user(email=admin_email)
    if(user is None) :
        print("Initializing admin user")
        encrypted_password = utils.encrypt_password('changeit')
        user_datastore.create_user(name="superuser", email=admin_email, password=encrypted_password, roles=[ADMIN_ROLE])

def setupRoleManagementEndpoints(app, user_datastore) :
    @app.route("/user/addrole", methods=['PUT'])
    @http_auth_required
    @roles_required(ADMIN_ROLE)
    def addUserRole():
        target_user = request.form["user"]
        role_to_set = request.form["role"]
        user_datastore.add_role_to_user(target_user,role_to_set)
        return "Added role '{}' to '{}'".format(role_to_set, target_user), 200

    @app.route("/user/removerole", methods=['PUT'])
    @http_auth_required
    @roles_required(ADMIN_ROLE)
    def removeUserRole():
        target_user = request.form["user"]
        role_to_remove = request.form["role"]
        user_datastore.remove_role_from_user(target_user,role_to_remove)
        return "Removed role '{}' from '{}'".format(role_to_remove, target_user), 200

    @app.route("/user/delete", methods=['PUT'])
    @http_auth_required
    @roles_required(ADMIN_ROLE)
    def deleteUser():
        target_user = request.form["user"]
        user_datastore.delete_user(user_datastore.get_user(target_user))
        return "Deleted user '{}'".format( target_user), 200

    # Supporting default template SECURITY_POST_LOGIN_VIEW
    @app.route("/user/loginok", methods=['GET'])
    @login_required
    def loginOk():
        return "Welcome back '{}'".format(current_user.email), 200

    @app.route("/user/registerok", methods=['GET'])
    @login_required
    def registerOk():
        return "Registration successful. Welcome '{}'".format(current_user.email), 200


def configureSecurityMongoDb(app, user_mongodb_uri=None) :
    with app.app_context() :
        print("Configuring security setup with mongodb")
        app.config['DEBUG'] = True
        app.config['SECRET_KEY'] = 'super-secret'
        app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
        app.config['SECURITY_PASSWORD_SALT'] = 'saltit'
        # Default views
        app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
        app.config['SECURITY_SEND_PASSWORD_CHANGE_EMAIL'] = False
        app.config['SECURITY_REGISTERABLE'] = True
        app.config['SECURITY_CHANGEABLE'] = True

        app.config['SECURITY_POST_LOGIN_VIEW'] = "/user/loginok"
        app.config['SECURITY_POST_REGISTER_VIEW'] = "/user/registerok"

        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['SECURITY_LOGIN_URL'] = '/testlogin'
        # MongoDB Config
        # app.config['MONGODB_DB'] = 'csoh_db'
        # app.config['MONGODB_HOST'] = 'localhost'
        user_mongodb_uri = DEFAULT_MONGODB_URI if (user_mongodb_uri is None) else user_mongodb_uri
        print("Using '{}' as user mongo db".format(user_mongodb_uri))
        app.config['MONGODB_HOST'] = user_mongodb_uri

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

        # Setup Flask-Security
        user_datastore = MongoEngineUserDatastore(db, User, Role)
        security = Security(app, user_datastore)

        initAdminUser(user_datastore)
        setupRoleManagementEndpoints(app, user_datastore)


        return db, user_datastore, security




# @app.route('/apchange', methods=['POST'])
# @http_auth_required
# @roles_required(ADMIN_ROLE)
# def adminChangePassword():
#         new_pass = utils.encrypt_password(request.form.get("pass"))
#         user = user_datastore.get_user(current_user.email)
#         user.password = new_padss
#         user_datastore.put(user)
#         return "Password changed", 200
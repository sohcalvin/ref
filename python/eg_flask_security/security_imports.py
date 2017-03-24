from flask import request
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, utils, roles_required, http_auth_required, current_user
ADMIN_ROLE = "admin"

def initAdminUser(user_datastore) :
    role = user_datastore.find_role(ADMIN_ROLE)
    if(role is None) :
        print("Initializing admin role")
        user_datastore.create_role(name=ADMIN_ROLE, description="Administrator")

    user = user_datastore.find_user(email="su@admin")
    if(user is None) :
        print("Initializing admin user")
        encrypted_password = utils.encrypt_password('changeit')
        user_datastore.create_user(name="superuser", email="su@admin", password=encrypted_password, roles=[ADMIN_ROLE])

def setupRoleManagementEndpoints(app) :
    @app.route("/addrole", methods=['GET', 'POST'])
    @roles_required(ADMIN_ROLE)
    @http_auth_required
    def addRole():

        return "Added role", 200


def configureSecurityMongoDb(app) :
    with app.app_context() :
        print("Configuring security setup with mongodb")
        app.config['DEBUG'] = True
        app.config['SECRET_KEY'] = 'super-secret'
        app.config['SECURITY_REGISTERABLE'] = False
        app.config['SECURITY_CHANGEABLE'] = True
        app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
        app.config['SECURITY_PASSWORD_SALT'] = 'saltit'
        # app.config['WTF_CSRF_ENABLED'] = False
        # app.config['SECURITY_LOGIN_URL'] = '/testlogin'
        # MongoDB Config
        app.config['MONGODB_DB'] = 'csoh_db'
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

        # Setup Flask-Security
        user_datastore = MongoEngineUserDatastore(db, User, Role)
        security = Security(app, user_datastore)

        initAdminUser(user_datastore)
        setupRoleManagementEndpoints(app)


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
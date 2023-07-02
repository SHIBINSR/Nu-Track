from flask import Flask
from main.extensions import db,cors
from werkzeug.security import generate_password_hash
from sqlalchemy import text

app=Flask(__name__,instance_relative_config=True)
app.config.from_prefixed_env()

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:password@localhost:3306/nutrack"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=True
app.config['UPLOAD_FOLDER'] = "static"


db.init_app(app)
cors.init_app(app)

from main.Services.models import *
from main.Services.views import services
app.register_blueprint(services)

from main.Client.models import *
from main.Client.views import client
app.register_blueprint(client)

from main.Vendor.models import *
from main.Vendor.views import vendor
app.register_blueprint(vendor)

from main.Plans.models import *
from main.Plans.views import plans
app.register_blueprint(plans)

# from main.user.models import *
from main.user.models import User
from main.user.views import user
app.register_blueprint(user)



# @app.before_first_request
# def insert_admin():
#     try:
#         print("started")
#         if not User.query.filter_by(email="admin@gmail.com").first(): 
#             print("hiiii")
#             add_admin =User(name="admin",Phone_number=34567890,email="admin@gmail.com",password="admin")
            
            
#             db.session.add(add_admin)
#             db.session.commit()
#         else:
#             print("admin already exist")
#     except Exception as e:
#         return str(e)
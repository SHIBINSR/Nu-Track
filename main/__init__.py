from flask import Flask
from main.extensions import db

app=Flask(__name__,instance_relative_config=True)
app.config.from_prefixed_env()

app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:password@localhost:3306/nutrack"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=True

db.init_app(app)

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
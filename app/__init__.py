from flask import Flask 
from app.endpoints import ap
from app import users, endpoints
from app.users import user_print
app = Flask(__name__)
app.register_blueprint(ap)
app.register_blueprint(user_print)
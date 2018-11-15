from flask import Flask
from app.views.users import user_print
from app.views.parcels import ap

app = Flask(__name__)
app.register_blueprint(ap)
app.register_blueprint(user_print)

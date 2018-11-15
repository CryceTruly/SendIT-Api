from flask import Flask
from flask_mail import Mail,Message

from app.views.parcels import ap
from app.views.users import user_print

app = Flask(__name__)
mail = Mail(app)


app.register_blueprint(ap)
app.register_blueprint(user_print)
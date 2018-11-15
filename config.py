import os
from app import app
'''
environment config
'''
class Config():
    DEBUG=True
    TESTING=True
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.environ.get('trulysEmail')
    app.config['MAIL_PASSWORD'] = os.environ.get('trulysPass')
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = True


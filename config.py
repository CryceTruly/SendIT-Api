import os
from app import app

#------------------INITIAL CONFIGURATIONS-----------------------------
class BaseConfig(object):
    DEBUG=False

#------------------DEVELOPMENT ENVIRONMENT CONFIGURATIONS-----------------------------
class DevConfig(BaseConfig):
    DEBUG=True
    TESTING=True
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'crycetruly@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Xvq6thC++'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = True
#------------------PRODUCTION ENVIRONMENT CONFIGURATIONS-----------------------------
class ProdConfig(BaseConfig):
    DEBUG=False

#------------------PRODUCTION ENVIRONMENT CONFIGURATIONS-----------------------------
class TestConfig(BaseConfig):
    DEBUG=True




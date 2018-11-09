import os

#------------------INITIAL CONFIGURATIONS-----------------------------
class BaseConfig(object):
    DEBUG=False

#------------------DEVELOPMENT ENVIRONMENT CONFIGURATIONS-----------------------------
class DevConfig(BaseConfig):
    DEBUG=True
    TESTING=True
#------------------PRODUCTION ENVIRONMENT CONFIGURATIONS-----------------------------
class ProdConfig(BaseConfig):
    DEBUG=False

#------------------PRODUCTION ENVIRONMENT CONFIGURATIONS-----------------------------
class TestConfig(BaseConfig):
    DEBUG=True




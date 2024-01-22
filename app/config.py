
import os

class BaseConfig(object):
    SITE_NAME = "Hackable"
    
    SECRET_KEY = os.environ.get("SECRET_KEY", None)
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")



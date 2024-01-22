from flask import Flask, render_template

from . import config

def register_extensions(app: Flask) -> None:
    
    from .database import db
    db.init_app(app)
    
    from .assets import assets
    assets.init_app(app)

def register_blueprints(app: Flask) -> None:
    
    from app.auth import auth
    app.register_blueprint(auth)

def create_app(config: config.BaseConfig = config.BaseConfig()) -> Flask:
    
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    register_extensions(app)
    register_blueprints(app)
    
    @app.route("/")
    def index():
        return render_template("index.html")
    
    return app
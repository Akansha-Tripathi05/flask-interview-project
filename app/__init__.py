from flask import Flask
from .extensions import db, ma, jwt
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    from .auth.routes import auth_bp
    from .inventory.routes import inv_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(inv_bp, url_prefix='/inventory')
    with app.app_context():
        db.create_all()
    return app
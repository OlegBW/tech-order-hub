from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .database import init_app

app = Flask(__name__)
app.config.from_pyfile('development.cfg', silent=True)
jwt = JWTManager(app)
CORS(app)
init_app(app)

from .registration import registration_blueprint
app.register_blueprint(registration_blueprint)

from .login import login_blueprint
app.register_blueprint(login_blueprint)

from .products import products_blueprint
app.register_blueprint(products_blueprint)

from .orders import orders_blueprint
app.register_blueprint(orders_blueprint)

from .invoices import invoices_blueprint
app.register_blueprint(invoices_blueprint)
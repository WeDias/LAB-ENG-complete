from flask import Flask
from models import base
from controllers import calculadora_controller, logs_controller, index_controller

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(calculadora_controller)
app.register_blueprint(logs_controller)
app.register_blueprint(index_controller)

base.init_app(app)
with app.app_context():
    base.create_all()

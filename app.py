from flask import Flask
from models import base
from controllers import calculadora, logs

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(calculadora)
app.register_blueprint(logs)

base.init_app(app)
with app.app_context():
    base.create_all()

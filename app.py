from flask import Flask
from models import base

app = Flask(__name__)
app.config.from_object('config')

base.init_app(app)
with app.app_context():
    base.create_all()

if __name__ == '__main__':
    app.run()

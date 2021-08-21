from flask import Blueprint, render_template
from models import base, OperationType, Log


index = Blueprint('home', __name__)


@index.route('/', methods=['GET'])
def getindex():
    return render_template('index.html')

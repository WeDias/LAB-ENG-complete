from flask import Blueprint, render_template


index = Blueprint('home', __name__)


@index.route('/', methods=['GET'])
def getindex():
    return render_template('index.html')

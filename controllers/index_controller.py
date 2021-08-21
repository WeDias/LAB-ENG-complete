from flask import Blueprint, render_template


index_controller = Blueprint('index_controller', __name__)


@index_controller.route('/', methods=['GET'])
def get_calculadora():
    return render_template('calculadora_template.html')

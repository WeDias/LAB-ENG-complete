from flask import Blueprint, render_template


calculadora_controller = Blueprint('calculadora_controller', __name__)


@calculadora_controller.route('/calculadora', methods=['GET'])
def get_calculadora():
    return render_template('calculadora_template.html')

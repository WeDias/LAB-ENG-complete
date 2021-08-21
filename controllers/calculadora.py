from flask import Blueprint, render_template


calculadora = Blueprint('calculadora', __name__)


@calculadora.route('/calculadora', methods=['GET'])
def get_calculadora():
    return render_template('calculadora.html')

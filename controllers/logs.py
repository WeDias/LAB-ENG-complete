from flask import Blueprint, render_template


logs = Blueprint('logs', __name__)


@logs.route('/logs', methods=['GET'])
def get_calculadora():
    return render_template('logs.html')

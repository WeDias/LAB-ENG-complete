from flask import Blueprint, render_template


logs_controller = Blueprint('logs_controller', __name__)


@logs_controller.route('/logs', methods=['GET'])
def get_calculadora():
    return render_template('logs_template.html')

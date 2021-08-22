from flask import Blueprint, render_template
from models import base, LogModel, OperationTypeModel


logs_controller = Blueprint('logs_controller', __name__)


@logs_controller.route('/logs', methods=['GET'])
def get_calculadora():
    data = base.session.query(LogModel, OperationTypeModel) \
        .join(OperationTypeModel, OperationTypeModel.opt_id == LogModel.log_opt_id) \
        .order_by(LogModel.log_id.desc()).all()
    return render_template('logs_template.html', data=data)

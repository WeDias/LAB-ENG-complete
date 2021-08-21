from flask import Blueprint, render_template
from models import base, OperationType, Log


index = Blueprint('home', __name__)


@index.route('/', methods=['GET'])
def getindex():

    # for log, optype in base.session.query(Log, OperationType).join(OperationType, OperationType.opt_id == Log.log_opt_id).all():
    #     print(log, optype)

    return render_template('index.html')

from datetime import datetime
from flask import Flask, request
from flask_cors import cross_origin
from models import base, LogModel


app = Flask(__name__)
app.config.from_object('config')
base.init_app(app)


@app.route('/log', methods=['POST'])
@cross_origin()
def post_log():
    try:
        new_log = LogModel(datetime.now().isoformat(), request.form['args'], int(request.form['id']))
        base.session.add(new_log)
        base.session.commit()
    except Exception as error:
        return {'status': 500, 'error': 'Ocorreu um erro ao processar a requisição'}
    else:
        return {'status': 200, 'success': True}

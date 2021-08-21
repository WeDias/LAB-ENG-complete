from math import cos
from flask import Flask, request


app = Flask(__name__)
app.config.from_object('config')


@app.route('/transcendental', methods=['GET'])
def get_result():
    try:
        result = cos(float(request.form["value1"]))
    except Exception as error:
        return {'status': 500, 'error': 'Ocorreu um erro ao processar a requisição'}
    else:
        return {'status': 200, 'result': result}

from flask import Flask, request
from flask_cors import cross_origin


app = Flask(__name__)
app.config.from_object('config')


@app.route('/elementary', methods=['POST'])
@cross_origin()
def post_result():
    try:
        result = eval(f'{request.form["value1"]} {request.form["operator"]} {request.form["value2"]}')
    except Exception as error:
        return {'status': 500, 'error': 'Ocorreu um erro ao processar a requisição'}
    else:
        return {'status': 200, 'result': result}

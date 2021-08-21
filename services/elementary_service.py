from flask import Flask, request


app = Flask(__name__)
app.config.from_object('config')


@app.route('/elementary', methods=['GET'])
def get_result():
    try:
        result = eval(f'{request.form["value1"]} {request.form["operator"]} {request.form["value2"]}')
    except Exception as error:
        return {'status': 500, 'error': 'Ocorreu um erro ao processar a requisição'}
    else:
        return {'status': 200, 'result': result}

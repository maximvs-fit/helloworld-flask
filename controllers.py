from app import app
from flask import render_template, request


@app.route('/')
@app.route('/ola')
def hello_world():
    return render_template('ola.html')


@app.route('/form', methods=['GET'])
def formulario_get():
    print('chamou o GET')
    return render_template('form.html')


@app.route('/form', methods=['POST'])
def formulario_post():
    print('Isso é um POST feito por', request.form['nome'])
    return render_template('form.html')

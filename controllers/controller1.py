from flask import Blueprint, render_template, session, request, url_for, redirect
from models.models1 import tarefas

tarefas_controllers = Blueprint('tarefas', __name__)

@tarefas_controllers.route('/')
def index():
    if 'username' in session:
        return render_template('html.html', tarefas = tarefas)
    return redirect(url_for('tarefas.hello'))


@tarefas_controllers.route('/hello')
def hello():
    return render_template("login.html")

@tarefas_controllers.route('/pegar', methods = ['POST'])
def pegar():
    nome = request.form.get('username')
    senha = request.form.get('password')

    for user in tarefas:
        if user["nome"] == nome and user["senha"] == senha:
            session['username'] = nome
            return render_template('html.html', tarefas = tarefas)
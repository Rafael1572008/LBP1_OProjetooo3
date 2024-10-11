from flask import Blueprint, render_template, session, request, url_for, redirect
from models.models1 import tarefas, users

tarefas_controllers = Blueprint(tarefas, __name__)

@tarefas_controllers.route('/')
def index():
    return render_template('html.html', tarefas = tarefas)

@tarefas_controllers.route('/hello')
def hello():
    return render_template("login.html")

@tarefas_controllers.route('/pegar')
def pegar():
    nome = request.args.get('username')
    senha = request.args.get('password')

    if users["nome"] == nome and users["senha"] == senha:
        redirect(url_for('index'))
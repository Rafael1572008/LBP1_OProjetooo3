from flask import Blueprint, render_template, session, request, url_for, redirect
from models.models1 import tarefas   #importaçãoes


tarefas_controllers = Blueprint('tarefas', __name__) #blueprint vindo de models, necessario para fazer a configuração


@tarefas_controllers.route('/')  #aba principal
def index():
    if 'username' in session:
        print (f"Bem Vindo {session['username']}")
        return render_template('html.html', tarefas = tarefas)
    return redirect(url_for('tarefas.login'))


@tarefas_controllers.route('/login')   #login
def login():
    return render_template("login.html", aviso = False)


tarefas_controllers.before_request   #não compreendi a onde aparece
def request_info():
    print("execulta antes da requisição")


@tarefas_controllers.route('/pegar', methods = ['POST', 'GET'])   ##rota para obter os dados
def pegar():
    nome = request.form.get('username')
    senha = request.form.get('password')

    for user in tarefas:
        if user["nome"] == nome and user["senha"] == senha:
            session['username'] = nome
            return redirect(url_for('tarefas.index'))
        
        aviso = "Senha ou usuario incorreto"
        return render_template('login.html', aviso = aviso)
    

#perguntar a onde se aplica o tempo de sessão
#não entendi midware
from flask import Blueprint, render_template, session, request, url_for, redirect
from models.models1 import users   #importaçãoes


mode = Blueprint('users', __name__) #blueprint vindo de models, necessario para fazer a configuração


@mode.route('/')  #aba principal
def index():
    if 'username' in session:
        print (f"Bem Vindo {session['username']}")
        return render_template('html.html', users = users)
    return redirect(url_for('users.login'))


@mode.route('/login')   #login
def login():
    return render_template("login.html", aviso = False)


@mode.before_request   #não compreendi a onde aparece
def request_info():
    print("execulta antes da requisição")


@mode.route('/pegar', methods = ['POST', 'GET'])   ##rota para obter os dados
def pegar():
    nome = request.form.get('username')
    senha = request.form.get('password')

    for user in users:
        if user.nome == nome and user.senha == senha:
            session['username'] = nome
            return redirect(url_for('users.index'))
        
    aviso = "Senha ou usuario incorreto"
    return render_template('login.html', aviso = aviso)
    
@mode.after_request
def after_request(response):
    print("execultar depois da requisição")
    return response


@mode.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('users.index'))
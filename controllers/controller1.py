from flask import Blueprint, render_template, session, request, url_for, redirect, flash
from models.models1 import users   # Importações

mode = Blueprint('users', __name__)  # Blueprint

@mode.route('/')  # Rota principal
def index():
    if 'username' in session:
        print(f"Bem Vindo {session['username']}")
        return render_template('html.html', users=users)
    return redirect(url_for('users.login'))

@mode.route('/login')   # Rota de login
def login():
    if 'username' in session:
        return redirect(url_for('users.index'))
    flash('Logado Com sucesso', 'success')  #Flash Menssager
    return render_template('login.html', aviso=False)

@mode.before_request   # Executa antes da requisição
def request_info():
    print("Executa antes da requisição")

@mode.route('/pegar', methods=['POST', 'GET'])   # Rota para obter dados
def pegar():
    if request.method == 'POST':
        nome = request.form.get('username')
        senha = request.form.get('password')

        # Verifica se o usuário e a senha estão corretos
        for user in users:
            if user.nome == nome and user.senha == senha:
                session['username'] = nome
                return redirect(url_for('users.index'))

        aviso = "Senha ou usuário incorreto"
        return render_template('login.html', aviso=aviso)

    # Se o método for GET, não há necessidade de verificar as credenciais aqui
    return render_template('login.html', aviso=False)

@mode.after_request
def after_request(response):
    print("Executa depois da requisição")
    return response

@mode.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('users.index'))
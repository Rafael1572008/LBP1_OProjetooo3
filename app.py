from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from controllers.controller1 import mode
from controllers.carrinho import prod

app = Flask(__name__)
app.secret_key = '9751a2bf696a9d8ff9a136d07173a9cbe5fe4996c50f576cca1f42c882b1c8f4'

rotas_publicas = ["users.pegar", "users.login", "users.index", "users.logout", "static"]
rotas_privadas = ["users.vip"]

app.register_blueprint(mode)
app.register_blueprint(prod)


@app.before_request
def request_info():
    rota = request.endpoint
    print(rota)
    print(session.get('user_type'))
    print('username')
    print(session)

    if rota in rotas_publicas or rota is None:
        if 'username' in session and rota == "user.pegar":
            return redirect(url_for('users.index'))
        return

    if rota in rotas_privadas:
        if 'username' not in session or session.get('user_type') != 'vip':
            print("entou")
            flash("Acesso negado. Você precisa ser um usuário VIP.", "erro")
            abort(403)

    if rota not in rotas_privadas and rota not in rotas_publicas and 'username' not in session:
        flash("Necessario ter sessão")
        abort(403)        

@app.after_request
def after_request(response):
    print("Executa depois da requisição")
    return response

@app.errorhandler(404)
def pageNotFound(e):
    print(e)
    return render_template("404.html"), 404

@app.errorhandler(403)
def pagewithoutaccess(e):
    return render_template("403.html"), 403

@app.errorhandler(500)
def servererror(e):
    return render_template("500.html"), 500

@app.errorhandler(Exception)
def generic(e):
    print(e)
    return render_template("generic.html"), 500

if __name__ == '__main__':
    app.run(debug=True)
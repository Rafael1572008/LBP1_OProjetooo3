from flask import Flask, render_template
from controllers.controller1 import mode
from controllers.carrinho import prod

app = Flask(__name__)

app.secret_key = 'xd_key'

app.register_blueprint(mode)
app.register_blueprint(prod)

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
    render_template('')

if (__name__) == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
from controllers.controller1 import mode
from controllers.carrinho import prod

app = Flask(__name__)

app.secret_key = 'xd_key'

app.register_blueprint(mode)
app.register_blueprint(prod)


if (__name__) == '__main__':
    app.run(debug=True)
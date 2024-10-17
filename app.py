from flask import Flask, render_template
from controllers.controller1 import mode

app = Flask(__name__)

app.secret_key = 'xd_key'

app.register_blueprint(mode)


if (__name__) == '__main__':
    app.run(debug=True)
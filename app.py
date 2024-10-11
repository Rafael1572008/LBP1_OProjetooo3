from flask import Flask, render_template
from controllers.controller1 import tarefas_controllers

app = Flask(__name__)

app.secret_key = 'xd'

app.register_blueprint(tarefas_controllers)


if (__name__) == '__main__':
    app.run(debug=True)



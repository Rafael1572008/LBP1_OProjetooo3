from flask import Flask
from controllers.controller1 import tarefas_controllers

app = Flask(__name__)
app.register_blueprint(tarefas_controllers)

@app.route('/hello')
def hello():
    return "Hello World"

if (__name__) == '__main__':
    app.run(debug=True)
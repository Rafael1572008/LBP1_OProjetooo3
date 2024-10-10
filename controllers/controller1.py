from flask import Blueprint, render_template
from models.models1 import tarefas

tarefas_controllers = Blueprint(tarefas, __name__)

@tarefas_controllers.route('/')
def index():
    return render_template('html.html', tarefas = tarefas)
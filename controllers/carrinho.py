from flask import Blueprint, render_template, session, request, url_for, redirect
from models.produtos import produtos   #importaçãoes

prod = Blueprint('produtos', __name__)

@prod.route('/carrinho')
def carr():
    return render_template('carrinho.html', produtos = produtos)

@prod.route('/carrinho/add', methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        r = request.form.get('produto_id')

    if request.method == 'GET':
        r = request.args.get('produto_id')

    for i in produtos:
        print (f"Produtos(id={i.id}, nome={i.nome}, preco={i.preco}, img={i.img})")

    return f"O produto tem indice {r}"    
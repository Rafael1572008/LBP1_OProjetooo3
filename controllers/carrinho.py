from flask import Blueprint, render_template, request, url_for, redirect, make_response
from models.produtos import produtos  # Importações

prod = Blueprint('produtos', __name__)

@prod.route('/carrinho')
def carr():
    return render_template('carrinho.html', produtos=produtos)

@prod.route('/carrinho/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        produto_id = request.form.get('produto_id')
    elif request.method == 'GET':
        produto_id = request.args.get('produto_id')

    # Redireciona para a rota /set_cookie com o ID do produto
    return redirect(url_for('produtos.set_cookie', produto_id= produto_id))

@prod.route('/set_cookie/<int:produto_id>')
def set_cookie(produto_id):
    # Busca o produto na lista de produtos
    for i in produtos:
        if i.id == produto_id:
            produto = i
            break 

    if produto:
        valor = f"Cód. Do produto: {produto.id}, nome: {produto.nome}, preco: {produto.preco}, img: {produto.img}"
        resp = make_response("Cookie has been set!")
        resp.set_cookie('car', valor, max_age = 60 * 60 * 24 * 7)  # 1 semana
        return resp

@prod.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('car')

    if cookie_value:
        return f"The cookie value is: {cookie_value}"
    return "Cookie not found!"

@prod.route('/del_cookie')
def del_cookie():
    resp = make_response("Cookie has been delet!")
    resp.set_cookie('car', '', max_age = 0)  # deletar
    return resp
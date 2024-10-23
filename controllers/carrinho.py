from flask import Blueprint, render_template, session, request, url_for, redirect, make_response
from models.produtos import produtos   # Importações

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

    for i in produtos:
        print(f"Produtos(id={i.id}, nome={i.nome}, preco={i.preco}, img={i.img})")

    return redirect(url_for('produtos.carr'))

@prod.route('/set_cookie')
def cookie(produto_id):

    for i in produtos:
        if i.id == produto_id:
            nome = i.nome
            preco = i.preco
            img = i.img
    
    valor = f"Cód. Do produto: {produto_id}, nome: {nome}, preco: {preco}, img: {img}"

    resp = make_response("Cookie has been set")
    resp.set_cookie('car', valor, max_age=60*60*24)  # 1 dia
    print(resp)
    return resp

@prod.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('car')

    if cookie_value:
        return f"The cookie value is: {cookie_value}"
    return "Cookie not found!"
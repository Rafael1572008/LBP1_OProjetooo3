from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash
from models.produtos import produtos  # Importações

prod = Blueprint('produtos', __name__)

@prod.route('/carrinho')
def carrinho():
    # Cria um dicionário para armazenar os produtos no carrinho com base nos cookies
    carrinho = {}
    for produto in produtos:
        quantidade = request.cookies.get(f'produto_{produto.id}', 0)

        if int(quantidade) > 0:
            total = produto.preco * int(quantidade)
            carrinho[produto.id] = {'nome': produto.nome, 'qntd': int(quantidade), 'total': total}

    return render_template('carrinho.html', produtos=produtos, carrinho=carrinho)

@prod.route('/carrinho/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        produto_id = request.args.get('id')
    elif request.method == 'POST':
        produto_id = request.form.get('id')
    else:
        print("oxi")

    resp = make_response(redirect(url_for('produtos.carrinho')))
    cookie = request.cookies.get(f'produto_{produto_id}')

    
    # Incrementa a quantidade do produto no cookie
    if cookie:
        resp.set_cookie(f'produto_{produto_id}', str(int(cookie) + 1))
    else:
        resp.set_cookie(f'produto_{produto_id}', "1")
    
    return resp

@prod.route('/carrinho/del', methods=['GET'])
def delete():
    produto_id = request.args.get('id')
    resp = make_response(redirect(url_for('produtos.carrinho')))
    cookie = request.cookies.get(f'produto_{produto_id}')
    
    # Decrementa a quantidade ou remove o cookie
    if cookie:
        if int(cookie) - 1 > 0:
            resp.set_cookie(f'produto_{produto_id}', str(int(cookie) - 1))
        else:
            resp.set_cookie(f'produto_{produto_id}', '', expires=0)  # Remove o cookie
    
    return resp
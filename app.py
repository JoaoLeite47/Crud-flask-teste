from resources import *
from service.service import ServiceTest

# cliente table


@app.route("/")  # get all cliente
def home():
    clientes = ServiceTest.selectClientes()
    return jsonify(clientes)


@app.route("/cliente/<cpf>/", methods=['GET'])  # get by cpf cliente FUNCIONAL
def cliente(cpf):
    cliente = ServiceTest.selectCliente(cpf)
    return jsonify(cliente)


@app.route("/cliente/novo/", methods=['POST'])  # post cliente FUNCIONAL
def cliente_post():
    userDetails = (request.json)
    criarCliente = ServiceTest.criarCliente(userDetails)
    if criarCliente == 0:
        return jsonify({"message": "Falha na criação do cliente"}), 400
    return jsonify({'message': 'Cliente criado com sucesso!'}), 201


@app.route('/cliente/update/<cpf>/', methods=['POST'])  # put cliente NÃO FUNCIONAL
def cliente_put(cpf):
    userDetails = (request.form)
    cpf = userDetails['cpf']
    cliente = ServiceTest.selectCliente(cpf, userDetails)
    if cliente == None:
        return jsonify({"message": "Cliente não encontrado"}), 400
    cliente_u = ServiceTest.updateCliente(userDetails)
    if cliente_u == 0:
        return jsonify({"message": "Falha na atualização do cliente"}), 400
    return jsonify({"status": "ok, alterado com sucesso"}), 201


# delete cliente FUNCIONAL
@app.route('/cliente/delete/<cpf>/', methods=['POST'])
def cliente_delete(cpf):
    cliente = ServiceTest.deleteCliente(cpf)
    if cliente == 0:
        return jsonify({"message": "Falha na remoção do cliente"}), 400
    return jsonify({"status": "ok, removido com sucesso"}), 201

# categoria table


@app.route("/categoria")  # get all categoria
def home_cat():
    categoria = ServiceTest.selectCategorias()
    return jsonify(categoria)


# get by cod_categ categoria FUNCIONAL
@app.route("/categoria/<cod_categ>/", methods=['GET'])
def cat_get(cod_categ):
    categoria = ServiceTest.selectCategoria(cod_categ)
    return jsonify(categoria)


@app.route("/categoria/novo/", methods=['POST'])  # post categoria FUNCIONAL
def categoria_post():
    userDetails = (request.json)
    criarCategoria = ServiceTest.criarCategoria(userDetails)
    if criarCategoria == 0:
        return jsonify({"message": "Falha na criação da categoria"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


# @app.route('/categoria/update/', methods=['POST'])  # put cliente NÃO FUNCIONAL
# def categoria_up():
#     userDetails = (request.form)
#     cod_categ = userDetails['cod_categ']
#     categoria = ServiceTest.updateCategoria(cod_categ)
#     if categoria == None:
#         return jsonify({"message": "Categoria não encontrada"}), 400
#     categoria_u = ServiceTest.updateCategoria(userDetails)
#     if categoria_u == 0:
#         return jsonify({"message": "Falha na atualização da categoria"}), 400
#     return jsonify("status" "ok, alterado com sucesso"), 201


# delete categoria FUNCIONAL
@app.route("/categoria/delete/<cod_categ>/", methods=['DELETE'])
def cat_delete(cod_categ):
    categoria = ServiceTest.deleteCategoria(cod_categ)
    if categoria == 0:
        return jsonify({"message": "Falha na remoção da categoria"}), 400
    return jsonify({"message" "ok, deletado com sucesso"}), 201

# alocação table


@app.route("/alocacao")  # get all alocacao
def home_alocacao():
    alocacoes = ServiceTest.selectAlocacoes()
    return jsonify(alocacoes)


# get by id_aloc alocacao FUNCIONAL
@app.route("/alocacao/<id_aloc>/", methods=['GET'])
def aloc_get(id_aloc):
    alocacao = ServiceTest.selectAlocacao(id_aloc)
    return jsonify(alocacao)


@app.route("/alocacao/novo/", methods=['POST'])  # post alocacao  NAO FUNCIONAL
def alocacao_post():
    userDetails = (request.json)
    criarAlocacao = ServiceTest.criarAlocacao(userDetails)
    if criarAlocacao == 0:
        return jsonify({"message": "Falha na criação da alocacao"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


@app.route('/alocacao/update/', methods=['POST'])  # put cliente NÃO FUNCIONAL
def alocacao_up():
    userDetails = (request.form)
    id_aloc = userDetails['id_aloc']
    alocacao = ServiceTest.updateAlocacao(id_aloc)
    if alocacao == None:
        return jsonify({"message": "Alocacao não encontrada"}), 400
    alocacao_u = ServiceTest.updateAlocacao(userDetails)
    if alocacao_u == 0:
        return jsonify({"message": "Falha na atualização da alocacao"}), 400
    return jsonify({"status" "ok, alterado com sucesso"}), 201


# delete alocacao FUNCIONAL
@app.route('/alocacao/delete/<id_aloc>/', methods=['DELETE'])
def alocacao_delete(id_aloc):
    alocacao = ServiceTest.deleteAlocacao(id_aloc)
    if alocacao == 0:
        return jsonify({"message": "Falha na remoção da alocacao"}), 400
    return jsonify({"message" "ok, deletado com sucesso"}), 201

# carro table


@app.route("/carro")  # get all carros
def home_carro():
    carros = ServiceTest.selectCarros()
    return jsonify(carros)


# get by chassi carro FUNCIONAL
@app.route("/carro/<chassi>/", methods=['GET'])
def carro_get(chassi):
    carro = ServiceTest.selectCarro(chassi)
    return jsonify(carro)


@app.route("/carro/novo/", methods=['POST'])  # post carro FUNCIONAL
def carro_post():
    userDetails = (request.json)
    criarCarro = ServiceTest.criarCarro(userDetails)
    if criarCarro == 0:
        return jsonify({"message": "Falha na criação do carro"}), 400
    return jsonify("status" "ok, Alterado com sucesso"), 201


@app.route('/carro/update/', methods=['POST'])  # put cliente NÃO FUNCIONAL
def carro_up():
    userDetails = (request.form)
    chassi = userDetails['chassi']
    carro = ServiceTest.updateCarro(chassi)
    if carro == None:
        return jsonify({"message": "Carro não encontrado"}), 400
    carro_u = ServiceTest.updateCarro(userDetails)
    if carro_u == 0:
        return jsonify({"message": "Falha na atualização do carro"}), 400
    return jsonify({"status" "ok, alterado com sucesso"}), 201


@app.route('/carro/<chassi>/', methods=['DELETE'])  # delete carro FUNCIONAL
def carro_delete(chassi):
    carro = ServiceTest.deleteCarro(chassi)
    if carro == 0:
        return jsonify({"message": "Falha na remoção do carro"}), 400
    return jsonify({"message" "ok, deletado com sucesso"}), 201


if __name__ == '__main__':
    app.run(debug=True)

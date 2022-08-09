from resources import *
from service.service import ServiceTest


@app.route("/clientes")
def home():
    clientes = ServiceTest.selectClientes()
    return jsonify(clientes)


@app.route("/cliente", methods=['GET'])
def cliente():
    userDetails = (request.json)
    cliente = ServiceTest.selectCliente(userDetails)
    return jsonify(cliente)


@app.route("/cliente/novo", methods=['POST'])
def cliente_post():
    userDetails = (request.json)
    criarCliente = ServiceTest.criarCliente(userDetails)
    if criarCliente == 0:
        return jsonify({"message": "Falha na criação do cliente"}), 400
    return jsonify({'message': 'Cliente criado com sucesso!'}), 201


@app.route('/cliente/update/<cpf>', methods=['POST'])
def cliente_put(cpf):
    userDetails = (request.json)
    cliente = ServiceTest.updateCliente(cpf, userDetails)
    if cliente == None:
        return jsonify({"message": "Cliente não encontrado"}), 400
    if cliente == 0:
        return jsonify({"message": "Falha na atualização do cliente"}), 400
    return jsonify({"status": "ok, alterado com sucesso"}), 201


@app.route('/cliente/delete/<cpf>', methods=['GET'])
def cliente_delete(cpf):
    cliente = ServiceTest.deleteCliente(cpf)
    if cliente == 0:
        return jsonify({"message": "Falha na remoção do cliente"}), 400
    return jsonify({"status": "ok, removido com sucesso"}), 201


@app.route("/categorias")
def home_cat():
    categoria = ServiceTest.selectCategorias()
    return jsonify(categoria)


@app.route("/categoria", methods=['GET'])
def cat_get():
    userDetails = (request.json)
    categoria = ServiceTest.selectCategoria(userDetails)
    return jsonify(categoria)


@app.route("/categoria/novo", methods=['POST'])
def categoria_post():
    userDetails = (request.json)
    criarCategoria = ServiceTest.criarCategoria(userDetails)
    if criarCategoria == 0:
        return jsonify({"message": "Falha na criação da categoria"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


@app.route('/categoria/update', methods=['POST'])
def categoria_put():
    userDetails = (request.json)
    categoria = ServiceTest.updateCategoria(userDetails)
    if categoria == None:
        return jsonify({"message": "Cliente não encontrado"}), 400
    if categoria == 0:
        return jsonify({"message": "Falha na atualização da categoria "}), 400
    return jsonify({"status": "ok, alterado com sucesso"}), 201


@app.route('/categoria/delete/<cod_categ>', methods=['GET'])
def categoria_delete(cod_categ):
    categoria = ServiceTest.deleteCategoria(cod_categ)
    if categoria == 0:
        return jsonify({"message": "Falha na remoção da categoria"}), 400
    return jsonify({"status": "ok, removido com sucesso"}), 201


@app.route("/alocacoes")
def home_alocacao():
    alocacoes = ServiceTest.selectAlocacoes()
    return jsonify(alocacoes)


@app.route("/alocacao", methods=['GET'])
def aloc_get():
    userDetails = (request.json)
    alocacao = ServiceTest.selectAlocacao(userDetails)
    return jsonify(alocacao)


@app.route("/alocacao/novo", methods=['POST'])
def alocacao_post():
    userDetails = (request.json)
    criarAlocacao = ServiceTest.criarAlocacao(userDetails)
    if criarAlocacao == 0:
        return jsonify({"message": "Falha na criação da alocacao"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201

# @app.route('/alocacao/update', methods=['POST'])  # put cliente NÃO FUNCIONAL
# def alocacao_up():
#     userDetails = (request.json)
#     alocacao = ServiceTest.updateAlocacao(userDetails)
#     print(alocacao)
#     if alocacao == None:
#         return jsonify({"message": "Alocacao não encontrada"}), 400
#     # alocacao_u = ServiceTest.updateAlocacao(userDetails)
#     if alocacao == 0:
#         return jsonify({"message": "Falha na atualização da alocacao"}), 400
#     return jsonify({"status" "ok, alterado com sucesso"}), 201


@app.route('/alocacao/delete/<id_aloc>', methods=['GET'])
def alocacao_delete(id_aloc):
    cliente = ServiceTest.deleteAlocacao(id_aloc)
    if cliente == 0:
        return jsonify({"message": "Falha na remoção da Alocação"}), 400
    return jsonify({"status": "ok, removido com sucesso"}), 201


@app.route("/carros")
def home_carro():
    carros = ServiceTest.selectCarros()
    return jsonify(carros)


@app.route("/carro", methods=['GET'])
def carro_get():
    userDetails = (request.json)
    carro = ServiceTest.selectCarro(userDetails)
    return jsonify(carro)


@app.route("/carro/novo", methods=['POST'])
def carro_post():
    userDetails = (request.json)
    criarCarro = ServiceTest.criarCarro(userDetails)
    if criarCarro == 0:
        return jsonify({"message": "Falha na criação do carro"}), 400
    return jsonify("status" "ok, Alterado com sucesso"), 201


@app.route('/carro/update', methods=['POST'])
def carro_up():
    userDetails = (request.json)
    carro = ServiceTest.updateCarro(userDetails)
    if carro == None:
        return jsonify({"message": "Carro não encontrado"}), 400
    if carro == 0:
        return jsonify({"message": "Falha na atualização do carro"}), 400
    return jsonify({"status": "ok, alterado com sucesso"}), 201


@app.route('/carro/delete/<chassi>', methods=['GET'])
def carro_delete(chassi):
    carro = ServiceTest.deleteCarro(chassi)
    if carro == 0:
        return jsonify({"message": "Falha na remoção do carro"}), 400
    return jsonify({"status": "ok, removido com sucesso"}), 201


if __name__ == '__main__':
    app.run(debug=True)

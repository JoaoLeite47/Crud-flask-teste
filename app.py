from resources import *
from service.service import ServiceTest


@app.route("/clientes")
def home():
    clientes = ServiceTest.selectClientes()
    return jsonify(clientes)


@app.route("/cliente/<cpf>", methods=['GET'])
def cliente(cpf):
    cliente = ServiceTest.selectCliente(cpf)
    if cliente == []:
        return jsonify({"message": "Cliente não encontrado"}), 400
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
    categorias = ServiceTest.selectCategorias()
    return jsonify(categorias)


@app.route("/categoria/<cod_categ>", methods=['GET'])
def cat_get(cod_categ):
    categoria = ServiceTest.selectCategoria(cod_categ)
    if categoria == []:
        return jsonify({"message": "Categoria não encontrada"}), 400
    return jsonify(categoria)


@app.route("/categoria/novo", methods=['POST'])
def categoria_post():
    userDetails = (request.json)
    criarCategoria = ServiceTest.criarCategoria(userDetails)
    if criarCategoria == 0:
        return jsonify({"message": "Falha na criação da categoria"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


@app.route('/categoria/update/<cod_categ>', methods=['POST'])
def categoria_put(cod_categ):
    userDetails = (request.json)
    categoria = ServiceTest.updateCategoria(userDetails, cod_categ)
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


@app.route("/alocacao/<id_aloc>", methods=['GET'])
def aloc_get(id_aloc):
    alocacao = ServiceTest.selectAlocacao(id_aloc)
    if alocacao == []:
        return jsonify({"message": "Alocação não encontrada"}), 400
    return jsonify(alocacao)


@app.route("/alocacao/novo", methods=['POST'])
def alocacao_post():
    userDetails = (request.json)
    criarAlocacao = ServiceTest.criarAlocacao(userDetails)
    if criarAlocacao == 0:
        return jsonify({"message": "Falha na criação da alocacao"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


@app.route('/alocacao/update/<id_aloc>', methods=['POST'])
def alocacao_up(id_aloc):
    userDetails = (request.json)
    alocacao = ServiceTest.updateAlocacao(userDetails, id_aloc)
    if alocacao == None:
        return jsonify({"message": "Alocação não encontrada"}), 400
    if alocacao == 0:
        return jsonify({"message": "Falha na atualização da alocação"}), 400
    return jsonify({"status": "ok, alterado com sucesso"}), 201


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


@app.route("/carro/<chassi>", methods=['GET'])
def carro_get(chassi):
    carro = ServiceTest.selectCarro(chassi)
    if carro == []:
        return jsonify({"message": "Carro não encontrado"}), 400
    return jsonify(carro)


@app.route("/carro/novo", methods=['POST'])
def carro_post():
    userDetails = (request.json)
    criarCarro = ServiceTest.criarCarro(userDetails)
    if criarCarro == 0:
        return jsonify({"message": "Falha na criação do carro"}), 400
    return jsonify("status" "ok, Criado com sucesso"), 201


@app.route('/carro/update/<chassi>', methods=['POST'])
def carro_up(chassi):
    userDetails = (request.json)
    carro = ServiceTest.updateCarro(userDetails, chassi)
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

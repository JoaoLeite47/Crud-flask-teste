import json
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


@app.route("/cliente/", methods=['POST'])  # post cliente FUNCIONAL
def cliente_post():
    userDetails = (request.json)
    criarCliente = ServiceTest.criarCliente(userDetails)
    if criarCliente == 0:
        return jsonify({"message": "Falha na criação do cliente"}), 400
    return jsonify({'message': 'Cliente criado com sucesso!'}), 201


# @app.route('/cliente/update/', methods=['POST'])  # put cliente NÃO FUNCIONAL
# def cliente_put():
#     userDetails = (request.form)
#     cpf = userDetails['cpf']
#     cliente = ServiceTest.selectCliente(cpf)
#     if cliente == None:
#         return jsonify({"message": "Cliente não encontrado"}), 400
#     cliente_u = ServiceTest.updateCliente(userDetails)
#     if cliente_u == 0:
#         return jsonify({"message": "Falha na atualização do cliente"}), 400
#     return jsonify({"status": "ok, alterado com sucesso"}), 201


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


@app.route("/categoria/", methods=['POST'])  # post categoria FUNCIONAL
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
@app.route("/categoria/<cod_categ>/", methods=['DELETE'])
def cat_delete(cod_categ):
    categoria = ServiceTest.deleteCategoria(cod_categ)
    if categoria == 0:
        return jsonify({"message": "Falha na remoção da categoria"}), 400
    return jsonify({"message" "ok, deletado com sucesso"}), 201

# alocação table


@app.route("/alocacao")  # get all alocacao
def home_alocacao():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alocacao")
    data = cur.fetchall()
    return jsonify(data)


# get by id_aloc alocacao FUNCIONAL
@app.route("/alocacao/<id_aloc>/", methods=['GET'])
def aloc_get(id_aloc):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM alocacao WHERE id_aloc = %s", (id_aloc,))
    data = cur.fetchall()
    return jsonify(data)


@app.route("/alocacao/", methods=['POST'])  # post alocacao  NAO FUNCIONAL
def alocacao_post():
    userDetails = (request.json)
    dt_saida = userDetails['dt_saida']
    dt_entrega = userDetails['dt_entrega']
    cpf_fk = userDetails['cpf_fk']
    chassi_fk = userDetails['chassi_fk']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO alocacao (dt_saida, dt_entrega, cpf_fk, chassi_fk) VALUES (%s, %s, %s, %s,)", (dt_saida, dt_entrega, cpf_fk, chassi_fk))
    mysql.connection.commit()
    return ("status" "ok, Criado com sucesso")

# @app.route('/cliente/<cpf>/', methods=['PUT']) # put cliente NÃO FUNCIONAL
# def cliente_put(cpf):
#     userDetails = (request.form)
#     nome = userDetails['nome']
#     endereco = userDetails['endereco']
#     cur = mysql.connection.cursor()
#     cur.execute(
#         "UPDATE cliente SET nome = %s, endereco = %s WHERE cpf = %s", (nome, endereco, cpf))
#     mysql.connection.commit()
#     return ("status" "ok, alterado com sucesso")


# delete alocacao FUNCIONAL
@app.route('/alocacao/<id_aloc>/', methods=['DELETE'])
def alocacao_delete(id_aloc):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM alocacao WHERE id_aloc = %s", (id_aloc,))
    mysql.connection.commit()
    return ("message" "ok, deletado com sucesso")

# carro table


@app.route("/carro")  # get all carros
def home_carro():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM carro")
    data = cur.fetchall()
    return jsonify(data)


# get by chassi carro FUNCIONAL
@app.route("/carro/<chassi>/", methods=['GET'])
def carro_get(chassi):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM carro WHERE chassi = %s", (chassi,))
    data = cur.fetchall()
    return jsonify(data)

# @app.route("/alocacao/", methods=['POST'])  # post alocacao FUNCIONAL
# def alocacao_post():
#     userDetails = (request.json)
#     dt_saida = userDetails['dt_saida']
#     dt_entrega = userDetails['dt_entrega']
#     cpf_fk = userDetails['cpf_fk']
#     chassi_fk = userDetails['chassi_fk']
#     cur = mysql.connection.cursor()
#     cur.execute(
#         "INSERT INTO alocacao (dt_saida, dt_entrega, cpf_fk, chassi_fk) VALUES (%s, %s, %s, %s,)", (dt_saida, dt_entrega, cpf_fk, chassi_fk))
#     mysql.connection.commit()
#     return ("status" "ok, Criado com sucesso")

# @app.route('/cliente/<cpf>/', methods=['PUT']) # put cliente NÃO FUNCIONAL
# def cliente_put(cpf):
#     userDetails = (request.form)
#     nome = userDetails['nome']
#     endereco = userDetails['endereco']
#     cur = mysql.connection.cursor()
#     cur.execute(
#         "UPDATE cliente SET nome = %s, endereco = %s WHERE cpf = %s", (nome, endereco, cpf))
#     mysql.connection.commit()
#     return ("status" "ok, alterado com sucesso")


@app.route('/carro/<chassi>/', methods=['DELETE'])  # delete carro FUNCIONAL
def carro_delete(chassi):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM carro WHERE chassi = %s", (chassi,))
    mysql.connection.commit()
    return ("message" "ok, deletado com sucesso")


if __name__ == '__main__':
    app.run(debug=True)

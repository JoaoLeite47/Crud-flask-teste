from resources import *

# cliente table


@app.route("/")  # get all cliente
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cliente")
    data = cur.fetchall()
    return jsonify(data)


@app.route("/cliente/<cpf>/", methods=['GET'])  # get by cpf cliente FUNCIONAL
def cliente(cpf):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cliente WHERE cpf = %s", (cpf,))
    data = cur.fetchall()
    return jsonify(data)


@app.route("/cliente/", methods=['POST'])  # post cliente FUNCIONAL
def cliente_post():
    userDetails = (request.json)
    nome = userDetails['nome']
    endereco = userDetails['endereco']
    cpf = userDetails['cpf']
    cnh = userDetails['cnh']
    dt_nascimento = userDetails['dt_nascimento']
    rg = userDetails['rg']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO cliente (nome, endereco, cpf, cnh, dt_nascimento, rg) VALUES (%s, %s, %s, %s, %s, %s)", (nome, endereco, cpf, cnh, dt_nascimento, rg))
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


@app.route('/cliente/<cpf>/', methods=['DELETE'])  # delete cliente FUNCIONAL
def cliente_delete(cpf):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM cliente WHERE cpf = %s", (cpf,))
    mysql.connection.commit()
    return ("message" "ok, deletado com sucesso")

# categoria table


@app.route("/categoria")  # get all categoria
def home_cat():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categoria")
    data = cur.fetchall()
    return jsonify(data)


# get by cod_categ categoria FUNCIONAL
@app.route("/categoria/<cod_categ>/", methods=['GET'])
def cat_get(cod_categ):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM categoria WHERE cod_categ = %s", (cod_categ,))
    data = cur.fetchall()
    return jsonify(data)


@app.route("/categoria/", methods=['POST'])  # post categoria FUNCIONAL
def categoria_post():
    userDetails = (request.json)
    cod_categ = userDetails['cod_categ']
    descricao = userDetails['descricao']
    valor_diaria = userDetails['valor_diaria']
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO categoria (cod_categ, descricao, valor_diaria) VALUES (%s, %s, %s)", (cod_categ, descricao, valor_diaria))
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


# delete categoria FUNCIONAL
@app.route("/categoria/<cod_categ>/", methods=['DELETE'])
def cat_delete(cod_categ):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM categoria WHERE cod_categ = %s", (cod_categ,))
    mysql.connection.commit()
    return ("message" "ok, deletado com sucesso")

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

# @app.route("/alocacao/", methods=['POST'])  # post alocacao  NAO FUNCIONAL
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

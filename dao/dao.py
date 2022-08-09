# from resources import *

import mysql.connector
from mysql.connector import Error
from datetime import datetime


class TesteDao:
    def conectar() -> tuple:
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="locadora.db",
                auth_plugin='mysql_native_password'
            )
            if mydb.is_connected():
                db_Info = mydb.get_server_info()
                print("Processing on MySQL Server version", db_Info)
                cursor = mydb.cursor()
                cursor.execute("SELECT database();")
                cursor.fetchone()
            mycursor = mydb.cursor()
            return (mycursor, mydb)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def selectClientes(mycursor: object) -> list:
        mycursor.execute("SELECT * FROM Cliente")
        myresult = mycursor.fetchall()
        return myresult

    def selectCliente(mycursor: object, userDetails: dict) -> list:
        cpf = userDetails['cpf']
        mycursor.execute("SELECT * FROM Cliente WHERE cpf = %s", (cpf,))
        myresult = mycursor.fetchone()
        return myresult

    def criarCliente(mycursor: object, mydb: object, userDetails: dict) -> list:
        nome = userDetails['nome']
        endereco = userDetails['endereco']
        cpf = userDetails['cpf']
        cnh = userDetails['cnh']
        dt_nascimento = userDetails['dt_nascimento']
        rg = userDetails['rg']
        mycursor.execute("INSERT INTO Cliente (nome, endereco, cpf, cnh, dt_nascimento, rg) VALUES (%s, %s, %s, %s, %s, %s)",
                         (nome, endereco, cpf, cnh, dt_nascimento, rg))
        mydb.commit()
        return mycursor.rowcount

    def updateCliente(mycursor: object, mydb: object, cpf: str, userDetails: dict) -> list:
        cpf = userDetails['cpf']
        nome = userDetails['nome']
        endereco = userDetails['endereco']
        cnh = userDetails['cnh']
        dt_nascimento = userDetails['dt_nascimento']
        rg = userDetails['rg']
        mycursor.execute("UPDATE Cliente SET nome = %s, endereco = %s, cnh = %s, dt_nascimento = %s, rg = %s WHERE cpf = %s",
                         (nome, endereco, cnh, dt_nascimento, rg, cpf))
        mydb.commit()
        return mycursor.rowcount

    def deleteCliente(mycursor: object, mydb: object, cpf: str) -> list:
        mycursor.execute("DELETE FROM Cliente WHERE cpf = %s", (cpf,))
        mydb.commit()
        return mycursor.rowcount

    def selectCategorias(mycursor: object) -> list:
        mycursor.execute("SELECT * FROM Categoria")
        myresult = mycursor.fetchall()
        return myresult

    def selectCategoria(mycursor: object, userDetails: dict) -> list:
        cod_categ = userDetails['cod_categ']
        mycursor.execute(
            "SELECT * FROM Categoria WHERE cod_categ = %s", (cod_categ,))
        myresult = mycursor.fetchone()
        return myresult

    def criarCategoria(mycursor: object, mydb: object, userDetails: dict) -> list:
        descricao = userDetails['descricao']
        valor_diaria = userDetails['valor_diaria']
        mycursor.execute(
            "INSERT INTO Categoria (valor_diaria, descricao) VALUES (%s, %s)", (valor_diaria, descricao))
        mydb.commit()
        return mycursor.rowcount

    def updateCategoria(mycursor: object, mydb: object, userDetails: dict) -> list:
        cod_categ = int(userDetails['cod_categ'])
        descricao = userDetails['descricao']
        valor_diaria = userDetails['valor_diaria']
        sql = "UPDATE Categoria SET descricao ='" + \
            str(descricao)+"', valor_diaria ='"+str(valor_diaria) + \
            "' WHERE cod_categ ='"+str(cod_categ)+"'"
        mycursor.execute(
            sql)
        return mycursor.rowcount

    def deleteCategoria(mycursor: object, mydb: object, cod_categ: int) -> list:
        mycursor.execute(
            "DELETE FROM Categoria WHERE cod_categ = %s", (cod_categ,))
        mydb.commit()
        return mycursor.rowcount

    def selectAlocacoes(mycursor: object) -> list:
        mycursor.execute("SELECT * FROM Alocacao")
        myresult = mycursor.fetchall()
        return myresult

    def selectAlocacao(mycursor: object, userDetails: dict) -> list:
        id_aloc = userDetails['id_aloc']
        mycursor.execute(
            "SELECT * FROM Alocacao WHERE id_aloc = %s", (id_aloc,))
        myresult = mycursor.fetchone()
        return myresult

    def criarAlocacao(mycursor: object, mydb: object, userDetails: dict) -> list:
        cpf_fk = userDetails['cpf_fk']
        chassi_fk = userDetails['chassi_fk']
        dt_saida = userDetails['dt_saida']
        dt_entrega = userDetails['dt_entrega']
        id_aloc = userDetails['id_aloc']
        mycursor.execute("INSERT INTO Alocacao (cpf_fk, chassi_fk, dt_saida, dt_entrega, id_aloc) VALUES (%s, %s, %s, %s, %s)",
                         (cpf_fk, chassi_fk, dt_saida, dt_entrega, id_aloc))
        mydb.commit()
        return mycursor.rowcount

    # def updateAlocacao(mycursor: object, mydb: object, userDetails: dict) -> list:
    #     cpf_fk = userDetails['cpf_fk']
    #     chassi_fk = userDetails['chassi_fk']
    #     dt_saida = int(userDetails['dt_saida'])
    #     dt_entrega = int(userDetails['dt_entrega'])
    #     id_aloc = int(userDetails['id_aloc'])
    #     sql = "UPDATE Alocacao SET cpf_fk = '"+str(cpf_fk)+"', chassi_fk ='"+str(chassi_fk)+"', dt_saida = '"+str(dt_saida)+"', dt_entrega = '"+str(
    #         dt_entrega)+"' WHERE id_aloc = '"+str(id_aloc)+"'"
    #     mycursor.execute(sql)
    #     return mycursor.rowcount

    def deleteAlocacao(mycursor: object, mydb: object, cod_alocacao: int) -> list:
        mycursor.execute(
            "DELETE FROM Alocacao WHERE cod_alocacao = %s", (cod_alocacao,))
        mydb.commit()
        return mycursor.rowcount

    def selectCarros(mycursor: object) -> list:
        mycursor.execute("SELECT * FROM Carro")
        myresult = mycursor.fetchall()
        return myresult

    def selectCarro(mycursor: object, userDetails: dict) -> list:
        chassi = userDetails['chassi']
        mycursor.execute("SELECT * FROM Carro WHERE chassi = %s", (chassi,))
        myresult = mycursor.fetchone()
        return myresult

    def criarCarro(mycursor: object, mydb: object, userDetails: dict) -> list:
        chassi = userDetails['chassi']
        marca = userDetails['marca']
        modelo = userDetails['modelo']
        ano = userDetails['ano']
        cor = userDetails['cor']
        placa = userDetails['placa']
        categoria_fk = userDetails['categoria_fk']
        mycursor.execute("INSERT INTO Carro (chassi, marca, modelo, ano, cor, placa, categoria_fk) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                         (chassi, marca, modelo, ano, cor, placa, categoria_fk))
        mydb.commit()
        return mycursor.rowcount

    def updateCarro(mycursor: object, mydb: object, userDetails: dict) -> list:
        chassi = userDetails['chassi']
        marca = userDetails['marca']
        modelo = int(userDetails['modelo'])
        ano = int(userDetails['ano'])
        cor = userDetails['cor']
        placa = userDetails['placa']
        categoria_fk = int(userDetails['categoria_fk'])
        sql = "UPDATE Carro SET marca = '"+str(marca)+"', modelo ='"+str(modelo)+"', ano = '"+str(ano)+"', cor = '"+str(
            cor)+"', placa = '"+str(placa)+"', categoria_fk = '"+str(categoria_fk)+"' WHERE chassi = '"+str(chassi)+"'"
        mycursor.execute(sql)
        return mycursor.rowcount

    def deleteCarro(mycursor: object, mydb: object, chassi: str) -> list:
        mycursor.execute("DELETE FROM Carro WHERE chassi = %s", (chassi,))
        mydb.commit()
        return mycursor.rowcount


# conex = TesteDao.conectar()
# alocacao_user_datails = {
#     "cpf_fk": "123456789",
#     "chassi_fk": "123456789",
#     "dt_saida": 20200101,
#     "dt_entrega": 20200101,
#     "id_aloc": 1
# }
# TesteDao.updateAlocacao(conex[0], conex[1], alocacao_user_datails)

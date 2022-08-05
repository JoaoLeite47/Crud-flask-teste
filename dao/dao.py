# from flask_mysqldb import MySQL

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'locadora.db'

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

    def selectCliente(mycursor: object, cpf: str) -> list:
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

    def updateCliente(mycursor: object, mydb: object, userDetails: dict) -> list:
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

    def selectCategoria(mycursor: object, cod_categ: int) -> list:
        mycursor.execute(
            "SELECT * FROM Categoria WHERE cod_categ = %s", (cod_categ,))
        myresult = mycursor.fetchone()
        return myresult

    def criarCategoria(mycursor: object, mydb: object, userDetails: dict) -> list:
        descricao = userDetails['descricao']
        valor_diaria = userDetails['valor_diaria']
        mycursor.execute(
            "INSERT INTO Categoria (valor_diaria, valor_diaria) VALUES (%s, %s)", (valor_diaria, descricao))
        mydb.commit()
        return mycursor.rowcount

    def updateCategoria(mycursor: object, mydb: object, userDetails: dict,) -> list:
        cod_categ = userDetails['cod_categ']
        descricao = userDetails['descricao']
        valor_diaria = userDetails['valor_diaria']
        mycursor.execute(
            "UPDATE Categoria SET descricao = %s, valor_diaria = %s WHERE cod_categ = %s", (descricao, valor_diaria, cod_categ))
        mydb.commit()
        return mycursor.rowcount

    def deleteCategoria(mycursor: object, mydb: object, cod_categ: int) -> list:
        mycursor.execute("DELETE FROM Categoria WHERE cod_categ = %s", (cod_categ,))
        mydb.commit()
        return mycursor.rowcount
import string
from tkinter.tix import Form
from flask import Flask, request, render_template, jsonify, url_for, redirect
from flask import Flask, send_file
from flask_mysqldb import MySQL
import time
import sys
import re
import os


app = Flask(__name__)  # Inicializa a aplicação
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'locadora.db'
mysql = MySQL(app)


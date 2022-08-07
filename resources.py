from flask import Flask, request, render_template, jsonify, url_for, redirect
from flask import Flask, send_file
import json


app = Flask(__name__)  # Inicializa a aplicação

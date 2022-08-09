from flask import Flask, request, render_template, jsonify, url_for, redirect
from flask import Flask, send_file
import json
from flask_cors import CORS


app = Flask(__name__)  # Inicializa a aplicação

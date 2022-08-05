import string
from tkinter.tix import Form
from flask import Flask, request, render_template, jsonify, url_for, redirect
from flask import Flask, send_file

import time
import sys
import re
import os


app = Flask(__name__)  # Inicializa a aplicação

# mysql = MySQL(app)

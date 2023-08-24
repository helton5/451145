# importações
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# caminho do arquivo de banco de dados - sqlite
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'jogo.db')

# caminho para arquivos em outras pastas
caminhopai = os.path.dirname(path)
pasta1 = os.path.join(caminhopai, 'rotas/')
arquivo1 = os.path.join(pasta1, 'incluir.py')
arquivo3 = os.path.join(pasta1, 'listar.py')

pasta2 = os.path.join(caminhopai, 'modelo/')
arquivo2 = os.path.join(pasta2, 'jogo.py')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
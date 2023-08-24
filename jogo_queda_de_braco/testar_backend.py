from Config import *
from listar import *
from incluir import *
from modelo import *

# rota padrão
@app.route("/")
def inicio():
    return render_template("index2.html")

@app.route("/home")
def home():
    return render_template("index2.html")


@app.route("/novo_listar")
def novo_listar():
    return render_template("listar.html")

# inserindo a aplicação em um contexto :-/
with app.app_context():
    db.create_all()
    CORS(app)
    app.run(debug=True, host="0.0.0.0")
from Config import *
from modelo import *

@app.route("/listar")
def listar():
    # obter os dados da classe informada
    dados = db.session.query(Jogo).all()
    
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
      #return render_template('listar.html')
    
    #else:
      #return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})
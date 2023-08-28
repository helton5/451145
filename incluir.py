from Config import *
from modelo import *

@app.route("/incluir", methods=['POST'])
def incluir():
    dados = request.get_json()
    # cria o jogo
    nova = Jogo(**dados)
    # realiza a persistência do novo jogo
    db.session.add(nova)
    db.session.commit()
    meujson = {"resultado": "ok"}
    meujson.update({"detalhes": "ok"})
    return jsonify(meujson)
    #return render_template('index2.html')
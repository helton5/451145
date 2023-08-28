from Config import *
from Testar_jogo import run

# inserindo a aplicação em um contexto :-/
with app.app_context():
    run()
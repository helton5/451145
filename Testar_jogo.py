from Config import *
from modelo import Jogo

def run():
    print("TESTE DO JOGO")
    with app.app_context():
        p1= Jogo(score = 270, score2 = 300)   
        db.session.add(p1)
        db.session.commit()
        print(p1)

run()    
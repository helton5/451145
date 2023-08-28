from Config import *

class Jogo(db.Model):
    # atributos do jogo
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    score2 = db.Column(db.Integer)
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "score": self.score,
            "score2": self.score2,
        }
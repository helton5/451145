from Config import *

class Jogo(db.Model):
    # atributos do jogo
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Text)
    score2 = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.titulo + "[id="+str(self.id)+ "], " +\
            self.score + ", " + self.score2
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "score": self.score,
            "score2": self.score2,
            "genero": self.genero,
        }
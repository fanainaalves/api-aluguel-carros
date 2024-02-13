from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    nome = db.Column(db.String(100))
    placa = db.Column(db.String(10))
    valor_dia = db.Column(db.Float)
    status = db.Column(db.String(20))
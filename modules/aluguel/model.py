from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluguel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    data_inicio = db.Column(db.Date)
    data_final = db.Column(db.Date)
    status = db.Column(db.String(20))
    valor_pagamento = db.Column(db.Float)



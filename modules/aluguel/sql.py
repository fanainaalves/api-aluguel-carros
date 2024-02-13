from flask_sqlalchemy import SQLAlchemy
from psycopg2 import sql
db = SQLAlchemy()

class Aluguel(db.Model):
    __tablename__ = 'aluguel'
    id = db.Column(db.Integer, primary_key=True)
    id_veiculo = db.Column(db.Integer, nullable=False)
    id_cliente = db.Column(db.Integer, nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_final = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    valor_pagamento = db.Column(db.Float, nullable=False)

def criar_aluguel(id_veiculo, id_cliente, data_inicio, data_final, status, valor_pagamento):
    aluguel = Aluguel(
        id_veiculo=id_veiculo,
        id_cliente=id_cliente,
        data_inicio=data_inicio,
        data_final=data_final,
        status=status,
        valor_pagamento=valor_pagamento
    )
    db.session.add(aluguel)
    db.session.commit()
    return aluguel
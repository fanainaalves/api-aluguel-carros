from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiculo(db.Model):
    __tablename__ = 'veiculo'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(10), nullable=False)
    valor_dia = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

def criar_veiculo(tipo, nome, placa, valor_dia, status):
    veiculo = Veiculo(tipo=tipo, nome=nome, placa=placa, valor_dia=valor_dia, status=status)
    db.session.add(veiculo)
    db.session.commit()
    return veiculo
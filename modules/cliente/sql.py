from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)

def criar_cliente(nome, cpf):
    cliente = Cliente(nome=nome, cpf=cpf)
    db.session.add(cliente)
    db.session.commit()
    return cliente
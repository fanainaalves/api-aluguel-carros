from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from psycopg2 import sql
from aluguel import model
from modules.aluguel.model import Aluguel
from modules.cliente.model import Cliente
from modules.veiculo.model import Veiculo

var = model.Aluguel
# veiculo = model.Veiculo
# cliente = model.Cliente


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:fanaina@localhost/postgres'
db = SQLAlchemy(app)

aluguel1 = Aluguel(id_veiculo=1, id_cliente=1, data_inicio='2024-05-01', data_final='2024-05-05', status='Ativo', valor_pagamento=200.0)
aluguel2 = Aluguel(id_veiculo=2, id_cliente=2, data_inicio='2024-05-02', data_final='2024-05-06', status='Ativo', valor_pagamento=250.0)
aluguel3 = Aluguel(id_veiculo=3, id_cliente=3, data_inicio='2024-05-03', data_final='2024-05-07', status='Ativo', valor_pagamento=180.0)

db.session.add_all([aluguel1, aluguel2, aluguel3])
db.session.commit()

print("Dados de Aluguel inseridos com sucesso!")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
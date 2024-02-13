from .model import Aluguel
from ..cliente import Cliente

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

def buscar_aluguel_por_id(aluguel_id):
    return Aluguel.query.get(aluguel_id)

def listar_alugueis():
    return Aluguel.query.all()

def atualizar_aluguel(aluguel_id, data):
    aluguel = Aluguel.query.get(aluguel_id)
    if aluguel:
        for key, value in data.items():
            setattr(aluguel, key, value)
        db.session.commit()
        return aluguel
    return None

def excluir_aluguel(aluguel_id):
    aluguel = Aluguel.query.get(aluguel_id)
    if aluguel:
        db.session.delete(aluguel)
        db.session.commit()
        return True
    return False

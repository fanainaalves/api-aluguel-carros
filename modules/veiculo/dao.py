from ..model import Veiculo,db

def criar_veiculo(tipo, nome, placa, valor_dia, status):
    veiculo = Veiculo(
        tipo=tipo,
        nome=nome,
        placa=placa,
        valor_dia=valor_dia,
        status=status
    )
    db.session.add(veiculo)
    db.session.commit()
    return veiculo

def buscar_veiculo_por_id(veiculo_id):
    return Veiculo.query.get(veiculo_id)

def listar_veiculos():
    return Veiculo.query.all()

def atualizar_veiculo(veiculo_id, data):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        for key, value in data.items():
            setattr(veiculo, key, value)
        db.session.commit()
        return veiculo
    return None

def excluir_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        db.session.delete(veiculo)
        db.session.commit()
        return True
    return False
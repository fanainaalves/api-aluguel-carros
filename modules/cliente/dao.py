from .model import Cliente, db

def criar_cliente(nome, cpf):
    cliente = Cliente(
        nome=nome,
        cpf=cpf
    )
    db.session.add(cliente)
    db.session.commit()
    return cliente

def buscar_cliente_por_id(cliente_id):
    return Cliente.query.get(cliente_id)

def listar_clientes():
    return Cliente.query.all()

def atualizar_cliente(cliente_id, data):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        for key, value in data.items():
            setattr(cliente, key, value)
        db.session.commit()
        return cliente
    return None

def excluir_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        db.session.delete(cliente)
        db.session.commit()
        return True
    return False
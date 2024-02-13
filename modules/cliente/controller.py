from flask import jsonify

from .dao import criar_cliente, buscar_cliente_por_id, listar_clientes, atualizar_cliente, excluir_cliente
from .model import Cliente


@app.route('/api/clientes', methods=['POST'])
def criar_cliente_endpoint():
    data = request.get_json()
    cliente = criar_cliente(data['nome'], data['cpf'])
    return jsonify({'message': 'Cliente criado com sucesso!', 'cliente_id': cliente.id})

#buscar
@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def buscar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if cliente:
        return jsonify(cliente.__dict__)
    return jsonify({'message': 'Cliente não encontrado'}), 404

# listar
@app.route('/api/clientes', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.__dict__ for cliente in clientes])

# atualizar
@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(cliente, key, value)

    db.session.commit()
    return jsonify({'message': 'Cliente atualizado com sucesso!'})

# excluir
@app.route('/api/clientes/<int:cliente_id>', methods=['DELETE'])
def excluir_cliente(cliente_id):
    cliente = Cliente.query.get(cliente_id)
    if not cliente:
        return jsonify({'message': 'Cliente não encontrado'}), 404

    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente excluído com sucesso!'})

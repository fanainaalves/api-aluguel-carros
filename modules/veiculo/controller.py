from flask import jsonify

from .dao import criar_veiculo, buscar_veiculo_por_id, listar_veiculos, atualizar_veiculo, excluir_veiculo
from .model import Veiculo


@app.route('/api/veiculos', methods=['POST'])
def criar_veiculo_endpoint():
    data = request.get_json()
    veiculo = criar_veiculo(data['tipo'], data['nome'], data['placa'], data['valor_dia'], data['status'])
    return jsonify({'message': 'Veículo criado com sucesso!', 'veiculo_id': veiculo.id})

# buscar por id
@app.route('/api/veiculos/<int:veiculo_id>', methods=['GET'])
def buscar_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if veiculo:
        return jsonify(veiculo.__dict__)
    return jsonify({'message': 'Veículo não encontrado'}), 404

# listar
@app.route('/api/veiculos', methods=['GET'])
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return jsonify([veiculo.__dict__ for veiculo in veiculos])

# atualizar
@app.route('/api/veiculos/<int:veiculo_id>', methods=['PUT'])
def atualizar_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if not veiculo:
        return jsonify({'message': 'Veículo não encontrado'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(veiculo, key, value)

    db.session.commit()
    return jsonify({'message': 'Veículo atualizado com sucesso!'})

# excluir
@app.route('/api/veiculos/<int:veiculo_id>', methods=['DELETE'])
def excluir_veiculo(veiculo_id):
    veiculo = Veiculo.query.get(veiculo_id)
    if not veiculo:
        return jsonify({'message': 'Veículo não encontrado'}), 404

    db.session.delete(veiculo)
    db.session.commit()
    return jsonify({'message': 'Veículo excluído com sucesso!'})

from flask import Flask, request, jsonify
from .model import Aluguel, db

app = Flask(__name__)

# criar um novo aluguel
@app.route('/api/alugueis', methods=['POST'])
def criar_aluguel():
    data = request.get_json()
    novo_aluguel = Aluguel(
        id_veiculo=data['id_veiculo'],
        id_cliente=data['id_cliente'],
        data_inicio=data['data_inicio'],
        data_final=data['data_final'],
        status=data['status'],
        valor_pagamento=data['valor_pagamento']
    )
    db.session.add(novo_aluguel)
    db.session.commit()
    return jsonify({'message': 'Aluguel criado com sucesso!'}), 201

# buscar um aluguel por ID
@app.route('/api/alugueis/<int:aluguel_id>', methods=['GET'])
def buscar_aluguel(aluguel_id):
    aluguel = Aluguel.query.get(aluguel_id)
    if aluguel:
        return jsonify(aluguel.__dict__)
    return jsonify({'message': 'Aluguel não encontrado'}), 404

#Listar
@app.route('/api/alugueis', methods=['GET'])
def listar_alugueis():
    alugueis = Aluguel.query.all()
    return jsonify([aluguel.__dict__ for aluguel in alugueis])

#atualizar
@app.route('/api/alugueis/<int:aluguel_id>', methods=['PUT'])
def atualizar_aluguel(aluguel_id):
    aluguel = Aluguel.query.get(aluguel_id)
    if not aluguel:
        return jsonify({'message': 'Aluguel não encontrado'}), 404

    data = request.get_json()
    for key, value in data.items():
        setattr(aluguel, key, value)

    db.session.commit()
    return jsonify({'message': 'Aluguel atualizado com sucesso!'})

#excluir
@app.route('/api/alugueis/<int:aluguel_id>', methods=['DELETE'])
def excluir_aluguel(aluguel_id):
    aluguel = Aluguel.query.get(aluguel_id)
    if not aluguel:
        return jsonify({'message': 'Aluguel não encontrado'}), 404

    db.session.delete(aluguel)
    db.session.commit()
    return jsonify({'message': 'Aluguel excluído com sucesso!'})


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, jsonify
from models.CorredorPrincipal import CorredorPrincipal
from models.Pessoa import Pessoa

app = Flask(__name__)

# Lista de pessoas no CorredorPrincipal
corredor = CorredorPrincipal(1, 50)

@app.route('/entrar', methods=['POST'])
def entrar_no_corredor():
    """Permite que uma pessoa entre no CorredorPrincipal."""
    data = request.json
    nome = data.get('nome')
    origem = data.get('origem')
    pessoa = Pessoa(nome, "1", origem)

    if nome:
        corredor.adicionaPessoa(pessoa)
        return jsonify({"mensagem": f"{nome} entrou no CorredorPrincipal!", "corredor": corredor.getNome()}), 200
    return jsonify({"erro": "Nome não fornecido"}), 400


@app.route('/sair', methods=['POST'])
def sair_do_corredor():
    """Permite que uma pessoa saia do CorredorPrincipal para outra cidade."""
    data = request.json
    nome = data.get('nome')
    destino = data.get('destino')  # IP da outra cidade
    pessoa = Pessoa().getNome() == nome
    
    if nome in corredor.getListaPessoas().getNome():
        corredor.removePessoa(pessoa)
        return jsonify({"mensagem": f"{nome} saiu para {destino}!", "corredor": corredor.getNome()}), 200
    return jsonify({"erro": "Pessoa não encontrada"}), 400


@app.route('/listar', methods=['GET'])
def listar_pessoas():
    """Lista as pessoas no CorredorPrincipal."""
    return jsonify({"corredor_principal": corredor.getListaPessoas()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
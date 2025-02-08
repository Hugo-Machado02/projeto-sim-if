from flask import Flask, request, jsonify
from models import Pessoa, CorredorPrincipal

app = Flask(__name__)

corredorPrincipal = CorredorPrincipal()

@app.route('/receberPessoa', methods=['POST'])
def receberPessoa():
    dados = request.get_json()
    nome = dados.get('nome')
    sobrenome = dados.get('sobrenome', 'Sobrenome')
    origem = dados.get('origem', 'Desconhecida')
    novaPessoa = Pessoa(nome, sobrenome, origem)
    corredorPrincipal.adicionaPessoa(novaPessoa)
    print(f"{novaPessoa.getNome()} chegou ao CorredorPrincipal.")
    return jsonify({"mensagem": f"{novaPessoa.getNome()} entrou na cidade."}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
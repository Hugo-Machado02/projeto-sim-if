from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def obter_ips_cidades():
    # Obtém todos os IPs das cidades conectadas via OpenVPN
    resultado = subprocess.run(['ip', 'route', 'show'], capture_output=True, text=True)
    linhas = resultado.stdout.split('\n')
    cidades = {}
    for linha in linhas:
        partes = linha.split()
        if len(partes) > 2 and partes[0] != 'default':
            cidade_ip = partes[0]
            cidades[f"cidade_{cidade_ip.replace('.', '_')}"] = f"{cidade_ip}:5000"
    return cidades

cidades_conectadas = obter_ips_cidades()

@app.route('/enviar', methods=['POST'])
def enviar_pessoa(self, pessoa):
    data = request.json
    nome = pessoa.getNome()
    
    if not cidades_conectadas:
        return jsonify({"erro": "Nenhuma cidade disponível."}), 404
    
    destino = random.choice(list(cidades_conectadas.keys()))
    
    for p in CorredorPrincial.getListaPessoas():
        if p.getNome() == nome:
            url_destino = f"http://{cidades_conectadas[destino]}/receber"
            response = requests.post(url_destino, json={"nome": p.getNome})
            if response.status_code == 200:
                CorredorPrincial.removePessoa(p)
                return jsonify({"mensagem": f"{nome} foi enviado para {destino}."})
            else:
                return jsonify({"erro": "Falha ao enviar a pessoa."}), 500
    
    return jsonify({"erro": "Pessoa não encontrada."}), 404

@app.route('/receber', methods=['POST'])
def receber_pessoa():
    data = request.json
    nome = data.get("nome")
    if not nome:
        return jsonify({"erro": "Nome é obrigatório"}), 400
    
    pessoa = Pessoa(f"{nome}", f"{i + 1}")
    CorredorPrincial.adicionaPessoa(pessoa)
    return jsonify({"mensagem": f"{nome} chegou na cidade."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
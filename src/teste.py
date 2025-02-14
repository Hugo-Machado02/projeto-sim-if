import socket
import threading
import time
import random
import socketio
import psutil
from flask import Flask
from flask_socketio import SocketIO

PORTA = 5001
CIDADES = {}
conexaoClient = socketio.Client()

# Inicialização do servidor Flask com o SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Pega o IP do radmin VPN
def get_radmin_ip():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and addr.address.startswith("26."):
                return addr.address
    return None

# Recebe uma mensagem e envia um retorno de volta
@socketio.on('mensagem')
def handle_mensagem(data):
    print(f"📨 Mensagem recebida: {data}")
    socketio.emit('resposta', {'info': 'Mensagem processada'})

# Rota principal que retorna a mensagem "Servidor Rodando"
@app.route('/')
def index():
    return "Servidor Rodando"

# Procura outras cidades na rede
def procurarCidades():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORTA))
    
    while True:
        data, addr = sock.recvfrom(1024)
        if data.decode() == "DISCOVERY":
            sock.sendto(b"RESPONSE", addr)
        elif data.decode() == "RESPONSE":
            ip = addr[0]
            CIDADES[ip] = time.time()

# Vai enviar Broadcast para todas as cidades que se conectarem na rede
def enviaBroadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        sock.sendto(b"DISCOVERY", ("<broadcast>", PORTA))
        time.sleep(5)

# Escolhe uma cidade na lista de cidades ativas
def escolheCidade():
    if CIDADES:
        return random.choice(list(CIDADES.keys()))
    return None

# Conecta a uma cidade ativa
def conexaoCidade():
    while True:
        cidade = escolheCidade()
        if cidade:
            caminho = f"http://{cidade}:5000"
            try:
                conexaoClient.connect(caminho)
                print(f"Conexão realizada a {caminho}")
                return
            except Exception as e:
                print(f"Falha ao conectar a {caminho}: {e}")
        time.sleep(5)

# Envia uma mensagem ao Servidor
def enviaDados():
    while True:
        if conexaoClient.connected:
            conexaoClient.emit('mensagem', {'info': 'atualização'})
        time.sleep(2)

@conexaoClient.on('resposta')
def receber_dados(data):
    print(f"Informação recebida: {data}")

# Iniciar threads
threading.Thread(target=procurarCidades, daemon=True).start()
threading.Thread(target=enviaBroadcast, daemon=True).start()
threading.Thread(target=conexaoCidade, daemon=True).start()
threading.Thread(target=enviaDados, daemon=True).start()

# Iniciar o servidor WebSocket
if __name__ == "__main__":
    MEUIP = get_radmin_ip() or "0.0.0.0"
    socketio.run(app, host=MEUIP, port=5000)
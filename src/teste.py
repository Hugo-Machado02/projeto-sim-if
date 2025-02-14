import socket
import threading
import time
import random
import socketio
import psutil
from flask import Flask
from flask_socketio import SocketIO

PORTA = 5000
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
    sock.settimeout(2)

    while True:
        try:
            print("Cidades ativas:", CIDADES)
            data, addr = sock.recvfrom(1024)
            print(f"Pacote recebido: {data.decode()} de {addr}")
            
            if data.decode() == "DISCOVERY":
                sock.sendto(b"RESPONSE", addr)
                ip = addr[0]
                if ip not in CIDADES:
                    CIDADES[ip] = time.time()  # Adiciona IP e timestamp
                    print(f"Cidade {ip} encontrada e adicionada.")
                else:
                    print(f"Cidade {ip} já está na lista.")
                print("Cidades ativas:", CIDADES)  # Exibindo os IPs armazenados após cada adição
        except socket.timeout:
            # Timeout ocorre se não houver resposta em 2 segundos
            pass

# Vai enviar Broadcast para todas as cidades que se conectarem na rede
def enviaBroadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        sock.sendto(b"DISCOVERY", ("255.255.255.255", PORTA))  # Usando o endereço de broadcast direto
        print("Enviando Broadcast para descobrir cidades...")
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
            print("Enviando Dados")
            conexaoClient.emit('mensagem', {'info': 'Olá, Teste de Cidades'})  # Envia a mensagem desejada
            print("Mensagem 'Olá, Teste de Cidades' enviada")
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
import socket
import threading
import time
import random
import socketio
from flask import Flask
from flask_socketio import SocketIO

PORTA = 5001
CIDADES = {}
conexaoClient = socketio.Client()

# Inicialização do servidor Flask com o SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Procura outras cidades na rede
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

#Escolhe uma cidade na lista de cidades ativas
def escolheCidade():
    if CIDADES:
        return random.choice(list(CIDADES.keys()))
    return None

#conecta a uma cidade ativa
def conexaoCidade():
    while True:
        cidade = escolheCidade()
        if cidade:
            cominho = f"http://{cidade}:5000"
            try:
                conexaoClient.connect(cominho)
                print(f"Conexáo realizada a {cominho}")
                return
            except Exception as erro:
                print(f"Falha ao conectar a {cominho}: {erro}")
        time.sleep(5)


# Iniciar threads
threading.Thread(target=procurarCidades, daemon=True).start()
threading.Thread(target=conexaoCidade, daemon=True).start()

# Iniciar o servidor WebSocket
if __name__ == "__main__":
    threading.Thread(target=lambda: socketio.run(app, host="0.0.0.0", port=5000), daemon=True).start()

# Mantém o programa rodando
while True:
    time.sleep(1)
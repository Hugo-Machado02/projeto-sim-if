import socket, threading, random, socketio, psutil, time, os
from controller.geraElementos import cricacaoElementos
from controller.interface import interfaceGrafica
from utils.operacoes import imprimirCidade
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO

DELAY = 5
PORTA = 5000
CIDADES = {}
conexaoClient = socketio.Client()

load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
MAX_PESSOAS_CORREDOR = int(os.getenv("MAX_PESSOAS_CORREDOR"))
MAX_PESSOAS_SALAS = int(os.getenv("MAX_PESSOAS_SALAS"))
THREADS = int(os.getenv("THREADS"))  # Máximo de threads simultâneas
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))
CIDADE = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS, MAX_PESSOAS_CORREDOR, MAX_PESSOAS_SALAS)

#Inicia do servidor Flask com o SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Pega o IP do radmin VPN
def configuraRangeIp():
    for interface, IPsLocalizados in psutil.net_if_addrs().items():
        for ip in IPsLocalizados:
            if ip.family == socket.AF_INET and ip.address.startswith("26."):
                return ip.address
    return None

#Recebe uma mensagem e envia um retorno de volta
@socketio.on('pessoa')
def handle_mensagem(pessoa):
    print(f"Uma nova pessoa entrou: {pessoa}")
    socketio.emit('resposta', {'info': 'Pessoa Recebida!'})
    

# Procura outras cidades na rede
def procurarCidades():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORTA))
    sock.settimeout(DELAY)
    MEUIP = configuraRangeIp()

    while True:
        print("Cidades ativas:", CIDADES)
        data, ipLocalizado = sock.recvfrom(1024)

        if ipLocalizado[0] == MEUIP:
            continue

        if data.decode() == "DISCOVERY":
            print(f"Resposta enviada para {ipLocalizado}")
            ip = ipLocalizado[0]
            if ip not in CIDADES:
                CIDADES[ip] = time.time()  # Adiciona IP e timestamp
                print(f"Cidade {ip} encontrada e adicionada.")
            else:
                print(f"Cidade {ip} já está na lista.")
            print("Cidades ativas:", CIDADES)
            
#Vai enviar Broadcast para todas as cidades que se conectarem na rede
def enviaBroadcast():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        sock.sendto(b"DISCOVERY", ("255.255.255.255", PORTA))
        time.sleep(DELAY)
        
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
        time.sleep(DELAY)
        
# Envia uma mensagem ao Servidor
def enviaDados(nome):
    while True:
        if conexaoClient.connected:
            print(f"Pessoa {nome} saiu da cidade")
            conexaoClient.emit('pessoa', {'info': nome})
        time.sleep(DELAY)
        
@conexaoClient.on('resposta')
def receber_dados(data):
    print(f"Pessoa recebida: {data}")
    
# Iniciar threads


semaforoBlocos = threading.Semaphore(7)
semaforoSalas = threading.Semaphore(2)

listaThreadsBlocos = []
listaThreadsSalas = []

def corredorPrincipal():
    CorredorPrincipal = CIDADE.getCorredor()
    while True:
        listaDestinos = CIDADE.getlistaBlocos()
        if CorredorPrincipal.getQuantidadePessoas() > 0:
            CorredorPrincipal.executaCorredor(listaDestinos)
        time.sleep(0.5)

def CorredorBloco(bloco):
    corredor = bloco.getCorredor()
    destinosCorredor = bloco.getListaSalas()
    corredorPrincipal =CIDADE.getCorredor()
    while True:
        if corredor.getQuantidadePessoas() > 0:
            with semaforoBlocos:
                corredor.executaCorredor(destinosCorredor, corredorPrincipal)
        time.sleep(0.5)

def TreadsBlocos():
    random.shuffle(listaThreadsBlocos)
    for threadBloco in listaThreadsBlocos:
        threadBloco.start()

def salas(sala, bloco):
    corredor = bloco.getCorredor()
    while True:
        if sala.getQuantidadePessoas() > 0:
            with semaforoSalas:
                sala.executaSalas([corredor])
        time.sleep(2)

def TreadsSalas():
    random.shuffle(listaThreadsSalas)
    for threadSala in listaThreadsSalas:
        threadSala.start()

def finalizar_servidor():
    time.sleep(TEMPO_EXECUCAO)
    time.sleep(2)
    os._exit(0)
    

@app.route('/')
def Simulacao():
    threading.Thread(target=procurarCidades, daemon=True).start()
    threading.Thread(target=enviaBroadcast, daemon=True).start()
    threading.Thread(target=conexaoCidade, daemon=True).start()
    CorredorPrincipal = threading.Thread(target=corredorPrincipal)
    CorredorPrincipal.daemon = True
    CorredorPrincipal.start()

    blocos = CIDADE.getlistaBlocos()
    for bloco in blocos:
        CorredorBlocoThread = threading.Thread(target=CorredorBloco, args=(bloco,))
        CorredorBlocoThread.daemon = True
        listaThreadsBlocos.append(CorredorBlocoThread)
    TreadsBlocos()

    for bloco in blocos:
        for sala in bloco.getListaSalas():
            salaThread = threading.Thread(target=salas, args=(sala, bloco,))
            salaThread.daemon = True
            listaThreadsSalas.append(salaThread)
    TreadsSalas()

    frontThread = threading.Thread(target=interfaceGrafica, args=(CIDADE,), daemon=True)
    frontThread.daemon = True
    frontThread.start()

    finalizaThreads = threading.Thread(target=finalizar_servidor)
    finalizaThreads.daemon = True
    finalizaThreads.start()

    return "Simulação em andamento!"

if __name__ == '__main__':
    app.run(debug=True)
    MEUIP = configuraRangeIp() or "0.0.0.0"
    socketio.run(app, host=MEUIP, port=5000)

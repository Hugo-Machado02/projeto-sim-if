import time, os, threading, random, psutil, socketio, socket
from controller.geraElementos import cricacaoElementos
from controller.interface import interfaceGrafica
from utils.operacoes import imprimirCidade
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO

load_dotenv()

DELAY = 5
PORTA = 6000
CIDADES = {}
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
MAX_PESSOAS_CORREDOR = int(os.getenv("MAX_PESSOAS_CORREDOR"))
MAX_PESSOAS_SALAS = int(os.getenv("MAX_PESSOAS_SALAS"))
THREADS = int(os.getenv("THREADS"))  # Máximo de threads simultâneas
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))
CIDADE = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS, MAX_PESSOAS_CORREDOR, MAX_PESSOAS_SALAS)
conexaoClient = socketio.Client()
semaforoBlocos = threading.Semaphore(7)
semaforoSalas = threading.Semaphore(2)
listaThreadsBlocos = []
listaThreadsSalas = []

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
@socketio.on('mensagem')
def handle_mensagem(data):
    print(f"📨 Mensagem recebida: {data}")
    socketio.emit('resposta', {'info': 'Mensagem processada'})

def corredorPrincipal():
    CorredorPrincipal = CIDADE.getCorredor()
    while True:
        listaDestinos = CIDADE.getlistaBlocos()
        if CorredorPrincipal.getQuantidadePessoas() > 0:
            nomePessoa = CorredorPrincipal.executaCorredor(listaDestinos)
            if nomePessoa != False:
                print(f"{nomePessoa} Saiu da Cidade")
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

def procurarCidades():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", PORTA))
    sock.settimeout(DELAY)
    MEUIP = configuraRangeIp()

    while True:
        print("Cidades ativas:", CIDADES)
        try:
            data, ipLocalizado = sock.recvfrom(1024)
            if ipLocalizado[0] == MEUIP:
                continue

            if data.decode() == "DISCOVERY":
                print(f"Resposta enviada para {ipLocalizado}")
                ip = ipLocalizado[0]
                if ip not in CIDADES:
                    CIDADES[ip] = time.time()
                    print(f"Cidade {ip} encontrada e adicionada.")
                else:
                    print(f"Cidade {ip} já está na lista.")
                print("Cidades ativas:", CIDADES)
        except socket.timeout:
            print("Timeout alcançado, buscando novamente...")
            pass

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
def enviaDados():
    while True:
        if conexaoClient.connected:
            print("Enviando Dados")
            conexaoClient.emit('mensagem', {'info': 'Olá, Teste de Cidades'})
        time.sleep(DELAY)

@conexaoClient.on('resposta')
def receber_dados(data):
    print(f"Informação recebida: {data}")


def finalizar_servidor():
    time.sleep(TEMPO_EXECUCAO)
    time.sleep(2)
    os._exit(0)

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

# frontThread = threading.Thread(target=interfaceGrafica, args=(CIDADE,), daemon=True)
# frontThread.daemon = True
# frontThread.start()

finalizaThreads = threading.Thread(target=finalizar_servidor)
finalizaThreads.daemon = True
finalizaThreads.start()

if __name__ == '__main__':
    MEUIP = configuraRangeIp() or "0.0.0.0"
    socketio.run(app, host=MEUIP, port=5000)

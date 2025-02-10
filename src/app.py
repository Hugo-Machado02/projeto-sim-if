import time, os, threading, random
from controller.geraElementos import cricacaoElementos
from controller.interface import interfaceGrafica
from utils.operacoes import imprimirCidade
from dotenv import load_dotenv
from flask import Flask

load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
MAX_PESSOAS_CORREDOR = int(os.getenv("MAX_PESSOAS_CORREDOR"))
MAX_PESSOAS_SALAS = int(os.getenv("MAX_PESSOAS_SALAS"))
THREADS = int(os.getenv("THREADS"))  # Máximo de threads simultâneas
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))
CIDADE = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS, MAX_PESSOAS_CORREDOR, MAX_PESSOAS_SALAS)

app = Flask(__name__)

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

def finalizar_servidor():
    time.sleep(60)
    imprimirCidade()
    os._exit(0)

@app.route('/')
def Simulacao():
    time.sleep(5)
    CorredorPrincipal = threading.Thread(target=corredorPrincipal)
    CorredorPrincipal.daemon = True
    CorredorPrincipal.start()

    frontThread = threading.Thread(target=interfaceGrafica, args=(CIDADE,), daemon=True)
    frontThread.daemon = True
    frontThread.start()

    finalizaThreads = threading.Thread(target=finalizar_servidor)
    finalizaThreads.daemon = True
    finalizaThreads.start()

    return "Simulação em andamento!"

if __name__ == '__main__':
    app.run(debug=True)

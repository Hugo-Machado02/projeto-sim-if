import time, os, threading
from queue import Queue, Empty
from controller.geraElementos import cricacaoElementos
from dotenv import load_dotenv
from flask import Flask

# Carrega Variáveis de ambiente
load_dotenv()
NUM_BLOCOS = int(os.getenv("NUM_BLOCOS"))
NUM_SALAS = int(os.getenv("NUM_SALAS"))
NUM_PESSOAS = int(os.getenv("NUM_PESSOAS"))
MAX_PESSOAS_CORREDOR = int(os.getenv("MAX_PESSOAS_CORREDOR"))
MAX_PESSOAS_SALAS = int(os.getenv("MAX_PESSOAS_SALAS"))
THREADS = int(os.getenv("THREADS"))  # Máximo de threads simultâneas
TEMPO_EXECUCAO = int(os.getenv("TEMPO_EXECUCAO"))

app = Flask(__name__)
fimThreads = threading.Event()
semaforo = threading.Semaphore(THREADS)
filaTarefas = Queue()


if __name__ == '__main__':
    # Iniciar servidor Flask em uma thread separada
    flaskThread = threading.Thread(target=app.run, kwargs={'debug': False, 'threaded': True})
    flaskThread.start()

    # Finalizar servidor Flask
    print("Finalizando servidor Flask...")
    os._exit(0)

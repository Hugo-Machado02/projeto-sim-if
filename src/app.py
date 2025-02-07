import time, os, threading
from controller.interface import atualizar_interface
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
CIDADE = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS, MAX_PESSOAS_CORREDOR, MAX_PESSOAS_SALAS)

app = Flask(__name__)
fimThreads = threading.Event()
semaforo = threading.Semaphore(THREADS)
filaTarefas = Queue()

def simulacao():
    #Gera elemenetos
    listaBlocos = CIDADE.getlistaBlocos()

    # Função para adicionar a tarefa no semaforo
    def adicionar_tarefas():
        filaTarefas.put((1, CIDADE.getCorredor()))
        for bloco in listaBlocos:
            filaTarefas.put((2, bloco))
            for sala in bloco.getListaSalas():
                filaTarefas.put((3, sala, [bloco.getCorredor()]))

    adicionar_tarefas()

    # Processamento das tarefas
    def listaTarefas():
        while not fimThreads.is_set():
            execucaoTarefa = filaTarefas.get(timeout=0.1)

            if fimThreads.is_set():
                break 

            tipo = execucaoTarefa[0]

            #Direcionamento para a execução
            with semaforo:
                if tipo == 1:
                    execucaoTarefa[1].executaCorredor(listaBlocos)
                elif tipo == 2:
                    execucaoTarefa[1].getCorredor().executaCorredor(execucaoTarefa[1].getListaSalas())
                elif tipo == 3:
                    execucaoTarefa[1].executaSalas(execucaoTarefa[2])

            #Execução das Tarefas
            if not fimThreads.is_set():
                filaTarefas.put(execucaoTarefa)

    # Criando as threads
    threads = []
    for i in range(THREADS):
        thread = threading.Thread(target=listaTarefas, daemon=True)
        threads.append(thread)
        thread.start()

    # Esperar o tempo de execução e depois encerrar
    time.sleep(TEMPO_EXECUCAO)
    fimThreads.set()  # Sinaliza para todas as threads pararem imediatamente
    print("Parando threads...")

    #
    for i in range(THREADS):
        filaTarefas.put(None)

    for thread in threads:
        thread.join()

    print("Fim da simulação!")

if __name__ == '__main__':
    # Thread para rodar o Flask
    flaskThread = threading.Thread(target=app.run, kwargs={'debug': False, 'threaded': True})
    flaskThread.start()

    # Thread para rodar a interface gráfica no terminal
    frontThread = threading.Thread(target=atualizar_interface, args=(CIDADE,), daemon=True)
    frontThread.start()

    simulacao()
    os._exit(0)
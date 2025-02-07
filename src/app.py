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

def simulacao():
    cidade = cricacaoElementos(NUM_BLOCOS, NUM_SALAS, NUM_PESSOAS, MAX_PESSOAS_CORREDOR, MAX_PESSOAS_SALAS)
    listaBlocos = cidade.getlistaBlocos()

    # Adiciona as tarefas iniciais na fila
    def adicionar_tarefas():
        filaTarefas.put(("corredor_principal", cidade.getCorredor()))

        for bloco in listaBlocos:
            filaTarefas.put(("corredor_bloco", bloco))
            for sala in bloco.getListaSalas():
                filaTarefas.put(("sala", sala, [bloco.getCorredor()]))

    adicionar_tarefas()

    # Processamento das tarefas
    def listaTarefas():
        while not fimThreads.is_set():
            try:
                execucaoTarefa = filaTarefas.get(timeout=0.1)  # Reduz timeout para encerrar rapidamente
            except Empty:
                continue  # Se a fila estiver vazia, verifica fimThreads e tenta novamente

            if fimThreads.is_set():
                break  # Se o evento de fim foi ativado, interrompe imediatamente

            tipo = execucaoTarefa[0]

            with semaforo:
                if tipo == "corredor_principal":
                    execucaoTarefa[1].executaCorredor(listaBlocos)
                elif tipo == "corredor_bloco":
                    execucaoTarefa[1].getCorredor().executaCorredor(execucaoTarefa[1].getListaSalas())
                elif tipo == "sala":
                    execucaoTarefa[1].executaSalas(execucaoTarefa[2])

            if not fimThreads.is_set():
                filaTarefas.put(execucaoTarefa)  # Reinsere a tarefa na fila apenas se fimThreads não foi ativado

    # Criando as threads
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=listaTarefas, daemon=True)
        threads.append(t)
        t.start()

    # Esperar o tempo de execução e depois encerrar
    time.sleep(TEMPO_EXECUCAO)
    fimThreads.set()  # Sinaliza para todas as threads pararem imediatamente
    print("Parando threads...")

    # Inserir "sentinelas" para desbloquear todas as threads
    for _ in range(THREADS):
        filaTarefas.put(None)

    # Aguarda todas as threads finalizarem
    for t in threads:
        t.join()

    print("Fim da simulação!")

if __name__ == '__main__':
    # Iniciar servidor Flask em uma thread separada
    flaskThread = threading.Thread(target=app.run, kwargs={'debug': False, 'threaded': True})
    flaskThread.start()

    # Executar simulação
    simulacao()

    # Finalizar servidor Flask
    print("Finalizando servidor Flask...")
    os._exit(0)

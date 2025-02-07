from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
from dotenv import load_dotenv
import time, os

load_dotenv()
DELAY = float(os.getenv("TEMPO_DELAY"))

class CorredorPrincipal(Corredor):

    def __init__(self, nome, capacidade):
        super().__init__(nome, capacidade)

    def incluiPessoas(self, listaPessoas):
        for pessoa in listaPessoas:
            self.adicionaPessoa(pessoa)

    # Implementação do método abstrato
    def executaCorredor(self, listaDestinos):
        while True:
            pessoas = self.getListaPessoas()
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, self, listaDestinos)
                        
                    time.sleep(DELAY)
            else:
                break
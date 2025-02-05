from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
import time

class CorredorPrincipal(Corredor):

    def __init__(self, capacidade):
        super().__init__(capacidade)

    def incluiPessoas(self, listaPessoas):
        for pessoa in listaPessoas:
            self.adicionaPessoa(pessoa)

    # Implementação do método abstrato
    def executaCorredor(self, cidade, listaDestinos):
        while True:
            pessoas = self.getListaPessoas()
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, self, listaDestinos)
                        time.sleep(1)
                    imprimirCidade(cidade)
            else:
                print("Näo Possui mais Pessoas no Corredor principal")
                time.sleep(1)
                break
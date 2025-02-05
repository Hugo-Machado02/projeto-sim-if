from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
import time


class CorredorBlocos(Corredor):

    def __init__(self, capacidade):
        super().__init__(capacidade)

    # Implementação do método abstrato
    def executaCorredor(self, cidade, corredorBloco, listaDestinos):
        while True:
            pessoas = self.getListaPessoas()
            destinos = listaDestinos
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, corredorBloco, destinos)
                        imprimirCidade(cidade)
                        time.sleep(1)
            else:
                print("Não Possui Mais Pessoas no Corredor do Bloco - ")
                time.sleep(1)
                break
            
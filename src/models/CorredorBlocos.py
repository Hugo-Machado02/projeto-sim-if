from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
import time


class CorredorBlocos(Corredor):

    def __init__(self, capacidade):
        super().__init__(capacidade)

    # Implementação do método abstrato
    def executaCorredor(self, cidade, listaDestinos, nome):
        while True:
            pessoas = self.getListaPessoas()
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, self, listaDestinos)
                        imprimirCidade(cidade)
                        time.sleep(1)
            else:
                print(f"Não Possui Mais Pessoas no Corredor - {nome}")
                time.sleep(1)
                break
            
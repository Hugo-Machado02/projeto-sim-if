from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
import time


class CorredorBlocos(Corredor):

    def __init__(self, nome, capacidade):
        super().__init__(nome, capacidade)

    # Implementação do método abstrato
    def executaCorredor(self, cidade, listaDestinos, nome):
        while True:
            pessoas = self.getListaPessoas()
            if pessoas:
                for pessoa in pessoas:
                    if not continuarLocal(pessoa):
                        enviaLocal(pessoa, self, listaDestinos)
                        #imprimirCidade(cidade)
                    else:
                        print(f"{pessoa.getNome()} Decidiu ficar no Local")
                        print("===============================================================================================")

                    time.sleep(0.4)
            else:
                break
            
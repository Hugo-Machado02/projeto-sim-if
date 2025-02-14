from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, selecionaPessoa

import requests

class CorredorPrincipal(Corredor):

    def __init__(self, nome, capacidade):
        super().__init__(nome, capacidade)

    def incluiPessoas(self, listaPessoas):
        for pessoa in listaPessoas:
            self.adicionaPessoa(pessoa)

    def executaCorredor(self, listaDestinos):
        listagem = listaDestinos
        pessoa = selecionaPessoa(self.getListaPessoas())
        if not continuarLocal(pessoa):
            continuaCidade = continuarLocal(pessoa)
            if(continuaCidade == True):
                enviaLocal(pessoa, self, listagem)
                return False
            else:
                self.removePessoa(pessoa)
                return pessoa.getNome()
        print(f"\n-> {pessoa.getNome()} vai continuar no corredor principal\n===============================================================================================")
        return False
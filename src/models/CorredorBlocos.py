from models.Corredor import Corredor
from utils.operacoes import continuarLocal, enviaLocal, selecionaPessoa

class CorredorBlocos(Corredor):

    def __init__(self, nome, capacidade):
        super().__init__(nome, capacidade)

    def executaCorredor(self, listaDestinos, CorredorPrincipal):
        lista = listaDestinos + [CorredorPrincipal]
        pessoa = selecionaPessoa(self.getListaPessoas())
        decisao =  pessoa.getDecisao(lista)
        if not continuarLocal(pessoa):
            enviaLocal(pessoa, self, decisao)
from utils.operacoes import imprimirCidade
import time
class Bloco:
    
    # Construtor
    def __init__(self, nome, corredor, listaSalas):
        self.__nome = nome
        self.__corredor = corredor
        self.__listaSalas = listaSalas
        
    # Encapsulamento
    def getNome(self):
        return self.__nome

    def getCorredor(self):
        return self.__corredor
    
    def getListaSalas(self):
        return self.__listaSalas
    
    def adicionaPessoa(self, pessoa):
        self.getCorredor().adicionaPessoa(pessoa)

    # Funções
    def adicionaSala(self, sala):
        self.__listaSalas.append(sala)
        
    def removerSala(self, sala):
        if self.__listaSalas:
            self.__listaSalas.remove(sala)
        else:
            print("Não há nenhuma sala!")

    #Funcão de Ação da Classe execucaoBloco
    def execucaoBlocos(self, cidade, lista):
        if self.getCorredor().getListaPessoas():
            self.getCorredor().executaCorredor(cidade, lista, self.getNome())
            time.sleep(0.4)

        if self.__listaSalas:
            for sala in self.getListaSalas():
                sala.executaSalas(cidade, [self.getCorredor()])
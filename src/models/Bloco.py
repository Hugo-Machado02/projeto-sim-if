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
    def execucaoBlocos(self, cidade):
        corredorBloco = self.getCorredor()
        salas = self.getListaSalas()
        # for sala in salas:
        #     sala.executaSalas(sala, corredorBloco)
        #for responsável pelo corredor
        salas.append(cidade.getCorredor())
        self.getCorredor().executaCorredor(cidade, corredorBloco, salas)
        time.sleep(1)
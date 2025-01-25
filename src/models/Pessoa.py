import random

class Pessoa:
    #Construtor
    def __init__(self, nome, localAtual, destino):
        self.__nome = nome
        self.__localAtual = localAtual
        self.__espera = 0
        self.__destino = destino

    # encapsulamento e métodos
    def getNome(self):
        return self.__nome
    
    def getLocalAtual(self):
        return self.__localAtual
    
    def getEspera(self):
        return self.__espera
    
    # def setEspera(self, espera):
    #     self.__destino = espera

    def getDestino(self):
        return self.__destino
    
    def setDestino(self, destino):
        self.__destino = destino
    
    def decisao(self):
        return random.choice([0,1])
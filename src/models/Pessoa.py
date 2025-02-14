import random

class Pessoa:
    #Construtor 1
    def __init__(self, nome, sobrenome, origem):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__origem = origem
        self.__espera = 0

    # encapsulamento e métodos
    def getNome(self):
        return f"{self.__nome} {self.__sobrenome}"

    def getOrigem(self):
        return self.__origem
    
    def getEspera(self):
        return self.__espera

    def setEspera(self):
        if self.getEspera() == 0:
            self.__espera = 1
        else:
            self.__espera = 0
            
    #Decisao da Pessoa
    def getDecisao(self, opcoes):
        if not isinstance(opcoes, list):  # Garante que opcoes seja uma lista
            opcoes = [opcoes]
        return random.choice(opcoes)
    
    def decisaoSaida(self):
        return random.choice([True, False])
class Cidade:
    def __init__(self, nome, corredor, listaBlocos):
        self.__nome = nome
        self.__corredorPrincipal = corredor
        self.__listaBlocos = listaBlocos
    
    def getnome(self):
        return self.__nome
    
    def getcorredorPrincipal(self):
        return self.__corredorPrincipal
    
    def getlistaBlocos(self):
        return self.__listaBlocos
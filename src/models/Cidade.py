class Cidade:
    def __init__(self, nome, corredor, listaBlocos):
        self.__nome = nome
        self.__corredor = corredor
        self.__listaBlocos = listaBlocos
    
    def getNome(self):
        return self.__nome
    
    def getCorredor(self):
        return self.__corredor
    
    def getlistaBlocos(self):
        return self.__listaBlocos
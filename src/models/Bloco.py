class Bloco:
    
    # Construtor
    def __init__(self, corredor):
        self.__corredor = corredor
        self.__listaSalas = []
        
    # Encapsulamento
    def getCorredor(self):
        return self.__corredor
    
    def getListaSalas(self):
        return self.__listaSalas
         
    # Funções
    def adicionaSala(self, sala):
        self.__listaSalas.append(sala)
        
    def removerSala(self, sala):
        if self.__listaSalas:
            self.__listaSalas.remove(sala)
        else:
            print("Não há nenhuma sala!")
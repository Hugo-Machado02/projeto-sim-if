from abc import ABC, abstractmethod

class Corredor(ABC):
    
    def __init__(self, nome, capacidade):
        self.__nome = nome
        self.__capacidade = capacidade
        self.__listaPessoas = []
        
    # Encapsulamento
    def getNome(self):
        return self.__nome

    def getCapacidade(self):
        return self.__capacidade
    
    def getListaPessoas(self):
        return self.__listaPessoas
    
    def getQuantidadePessoas(self):
        return len(self.__listaPessoas)
        
    # Funções
    def adicionaPessoa(self, pessoa):
        self.__listaPessoas.append(pessoa)
        
    def removePessoa(self, pessoa):
        if self.__listaPessoas:
            self.__listaPessoas.remove(pessoa)
        else:
           print(f"----> Náo h[a pessoas no {self.getNome()}")
    
    #implementação do método abstrato
    @abstractmethod
    def executaCorredor(self):
        pass

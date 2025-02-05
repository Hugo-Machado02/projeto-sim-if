from utils.operacoes import continuarLocal, enviaLocal, imprimirCidade
import time

class Sala:

    def __init__(self, nome, capacidade):
        self.__nome = nome
        self.__capacidade = capacidade
        self.__status = 1
        self.__pessoas = []

    def getNome(self):
        return self.__nome
    
    
    def getCapacidade(self):
        return self.__capacidade
    
    
    def getStatus(self):
        return self.__status
    
    
    def __setStatus(self):
        if self.getQuantidadePessoas() == self.getCapacidade() and self.getCapacidade() == 1:
            self.__capacidade = 0

        elif self.getQuantidadePessoas() < self.getCapacidade() and self.getCapacidade() == 0:
            self.__capacidade = 1


    def getPessoas(self):
        return self.__pessoas
    
    
    def adicionaPessoa(self, pessoa):
        if self.__verificaCapacidade():
            self.__pessoas.append(pessoa)
            self.__setStatus()
            return True
        
        else:
            print("Sala Lotada de Alunos")
            return False
        

    def removePessoa(self, pessoa):
        if self.getQuantidadePessoas() > 0:
            self.__pessoas.remove(pessoa)
            self.__setStatus()
            return True
        
        else:
            print("A sala não Possui alunos para remover")
            return False

        
    def __verificaCapacidade(self):
        if self.getQuantidadePessoas() < self.getCapacidade():
            return True
        else:
            return False
        
    def getQuantidadePessoas(self):
        return len(self.getPessoas())
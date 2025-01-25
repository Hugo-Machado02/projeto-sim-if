class Sala:

    def __init__(self, nome, ocupacao):
        self.__nome = nome
        self.__ocupacao = ocupacao
        self.__status = 1
        self.__pessoas = []

    def getNome(self):
        return self.__nome
    
    
    def getOcupacao(self):
        return self.__ocupacao
    
    
    def getStatus(self):
        return self.__status
    
    
    def __setStatus(self):
        if self.quantidadePessoas() == self.getOcupacao() and self.getOcupacao() == 1:
            self.__ocupacao = 0

        elif self.quantidadePessoas() < self.getOcupacao() and self.getOcupacao() == 0:
            self.__ocupacao = 1


    def getPessoas(self):
        return self.__pessoas
    
    
    def entrar(self, pessoa):
        if self.__verificaCapacidade() :
            self.__pessoas.append(pessoa)
            self.__setStatus()
            return True
        
        else:
            print("Sala Lotada de Alunos")
            return False
        

    def sair(self, pessoa):
        if self.quantidadePessoas() > 0:
            self.__pessoas.remove(pessoa)
            self.__setStatus()
            return True
        
        else:
            print("A sala não Possui alunos para remover")
            return False

        
    def __verificaCapacidade(self):
        if self.quantidadePessoas() < self.getOcupacao():
            return True
        else:
            return False
        
    def quantidadePessoas(self):
        return len(self.getPessoas())
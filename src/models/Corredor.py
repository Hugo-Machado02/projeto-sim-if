import Pessoa

class Corredor:
    
    # Construtor
    def __init__(self):
        self.__capacidade = 40
        self.__listaPessoas = []
        
    # Encapsulamento
    def getCapacidade(self):
        return self.__capacidade
    
    def getListaPessoas(self):
        return self.__listaPessoas
        
    # Funções
    def adicionarPessoa(self, pessoa):
        self.__listaPessoas.append(pessoa)
        
    def removerPessoa(self, pessoa):
        if self.__listaPessoas:
            self.__listaPessoas.remove(pessoa)
        else:
            print("Não há nenhuma pessoa no corredor!")
            
    
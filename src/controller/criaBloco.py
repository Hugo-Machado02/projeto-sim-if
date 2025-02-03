from models.Bloco import Bloco
from models.Corredor import Corredor
from controller.criaSalas import criacaoSalas
nomes = ["Informatica", "Quimica", "Pedagogia", "Zootecnia", "Alimentos", "Núcleo Comum", "Administração", "API"]

def geraBlocos(numBlocos, numSalas):
    blocos = []
    for i in range(numBlocos):
        salas = criacaoSalas(numSalas)
        corredor = Corredor()
        bloco = Bloco(nomes[i], corredor, salas)
        blocos.append(bloco)
    return blocos
from models.Bloco import Bloco
from models.CorredorBlocos import CorredorBlocos
from controller.criaSalas import criacaoSalas
nomes = ["Informatica", "Quimica", "Pedagogia", "Zootecnia", "Alimentos", "Núcleo Comum", "Administração", "API"]

def geraBlocos(numBlocos, numSalas):
    blocos = []
    for i in range(numBlocos):
        salas = criacaoSalas(numSalas)
        corredor = CorredorBlocos(50)
        bloco = Bloco(nomes[i], corredor, salas)
        blocos.append(bloco)
    return blocos
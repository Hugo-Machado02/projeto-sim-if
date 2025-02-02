from models.Bloco import Bloco
from models.Corredor import Corredor
from controller.criaSalas import criacaoSalas
nomes = ["Informatica", "Quimica", "Pedagogia", "Zootecnia", "Alimentos", "Núcleo Comum", "Administração", "API"]
blocos = []

def geraBlocos(numBlocos, numSalas):
    for i in range(numBlocos):
        nome = f"Bloco - {nomes[i]}"
        salas = criacaoSalas(numSalas)
        corredor = Corredor()
        bloco = Bloco(nome, corredor, salas)
        blocos.append(bloco)

    return blocos
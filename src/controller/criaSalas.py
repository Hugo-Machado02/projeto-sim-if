from models.Sala import Sala

listaSalas = []

def criacaoSalas(num):
    for i in range(num):
        pessoa = Sala(f"Sala {i + 1}", f"Informatica {i + 1}")
        listaSalas.append(pessoa)
    return listaSalas
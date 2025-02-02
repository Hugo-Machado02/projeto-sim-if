from models.Sala import Sala

def criacaoSalas(num):
    listaSalas = []
    for i in range(num):
        sala = Sala(f"Sala {i + 1}", 5)
        listaSalas.append(sala)
    return listaSalas
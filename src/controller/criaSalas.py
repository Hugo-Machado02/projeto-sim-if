from models.Sala import Sala

def criacaoSalas(numeroSalas):
    listaSalas = []
    for i in range(numeroSalas):
        sala = Sala(f"Sala {i + 1}", 5)
        listaSalas.append(sala)
    return listaSalas
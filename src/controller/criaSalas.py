from models.Sala import Sala

def criacaoSalas(numeroSalas, maxPessoasSalas):
    listaSalas = []
    for i in range(numeroSalas):
        sala = Sala(f"Sala {i + 1}", maxPessoasSalas)
        listaSalas.append(sala)
    return listaSalas
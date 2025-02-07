from models.Cidade import Cidade
from models.CorredorPrincipal import CorredorPrincipal


def criacaoCidade(listaBlocos):
    corredor = CorredorPrincipal("Corredor Principal", 40)
    cidade = Cidade("Sim-IF", corredor, listaBlocos)
    return cidade
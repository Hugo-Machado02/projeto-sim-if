from models.Cidade import Cidade
from models.CorredorPrincipal import CorredorPrincipal


def criacaoCidade(listaBlocos):
    corredor = CorredorPrincipal(40)
    cidade = Cidade("Sim-IF", corredor, listaBlocos)
    return cidade
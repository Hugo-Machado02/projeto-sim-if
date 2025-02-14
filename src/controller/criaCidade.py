from models.Cidade import Cidade
from models.CorredorPrincipal import CorredorPrincipal


def criacaoCidade(listaBlocos):
    corredor = CorredorPrincipal("Corredor Principal", 40)
    cidade = Cidade("SymIF - Hugo", corredor, listaBlocos)
    return cidade